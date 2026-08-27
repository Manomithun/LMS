# Copyright (c) 2026, mano and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate,add_days, getdate

class BookIssue(Document):

	def before_insert(self):
        
		membership_of_member = self.get_membership()
		self.barrowed_date = nowdate()
		allowed_borrow_days = membership_of_member.borrow_days
		self.due_date = add_days(
								self.barrowed_date, 
								allowed_borrow_days
							)

	def validate(self):
		frappe.msgprint(str(self.status))
		book_copy = self.get_book_copy()
		membership_of_member = self.get_membership()
        
		# prevent changing the return_date of book once it has been set
		if(not self.is_new() and self.has_value_changed("return_date") and self.get_doc_before_save("return_date")):
			frappe.throw("Return Date can only be set once")

		# checking is this is a new document and adding the borrow date and due date while issuing the book
		if self.is_new():
			self.check_book_availability(book_copy)

			# number of book that student loanded till now
			issued_books = frappe.db.count(
				"Book Issue",
				{
					"member":self.member,
					"status":"Approved"
				}
			)
			if issued_books >= membership_of_member.max_book :
				frappe.throw(
                f"This member can borrow only {membership_of_member.max_book} books."
            )

		
		if self.status == "Returned":
			if not self.return_date:
				frappe.throw("Return date is required.")
			if getdate(self.return_date) < getdate(self.barrowed_date):
				frappe.throw("Return date cannot be before borrowed date.")
			if getdate(self.return_date) > getdate(nowdate()):
				frappe.throw("Return date cannot be in the future.")

		elif self.return_date:
			frappe.throw("Status must be 'Returned' when a return date is entered.")		



	def after_insert(self):
		book_copy = self.get_book_copy()
		self.change_book_copy_status(book_copy, "Approved")
		frappe.msgprint("Added Successfully.. book Issue is approved")
		book = self.get_book()
		book.refresh_book_statistics()


	def on_update(self):

        # while returning the book automatically calucalating the fine and if the fine is detected it created new doc for fine for a member
		if self.has_value_changed("status") and self.status == "Returned":
			book_copy = self.get_book_copy()
			membership_of_member = self.get_membership()
			self.book_return(membership_of_member,book_copy)


	def get_book_copy(self):
		# check if book is available
		book_copy_id = self.copyid
		book_copy =  frappe.get_doc("BookCopy",book_copy_id)
		return book_copy

	def get_book(self):
		book_id = self.get_book_copy().book_id
		book = frappe.get_doc("Book", {"name": book_id})
		return book

	def get_membership(self):
		# getting primary key of the member from the bookIssue doc
		member_id = self.member
		
		member = frappe.get_doc("Member",member_id)
		
		# getting primary key of the membership of the member to whom the was issued
		member_type_id = member.membertype
		
		# identifing the type of membership of the member
		membership_of_member = frappe.get_doc("MemberShip",member_type_id)

		return membership_of_member
		

			

#validating the book returning date and updaing the book Status
	def book_return(self,membership_of_member,book_copy):

		if getdate(self.return_date) >getdate(self.due_date):
			fine = self.calculate_fine(membership_of_member)
			if fine > 0:
				self.create_fine(fine)
				frappe.msgprint(f"fine applied {fine}")
		self.change_book_copy_status(book_copy,"Available")
		book = self.get_book()
		book.refresh_book_statistics()
		




# check if the book is available

	def check_book_availability(self,book_copy):
	
		if book_copy.status != "Available":
			frappe.throw("Book is not available for issue.")




# while issue book changing the status of the book status
	def change_book_copy_status(self,book_copy,status):
		book_copy.status = status
		book_copy.save()
			
# calculating fine for a member while returning book 

	def calculate_fine(self,membership_of_member):

		# find overdue_days to member based on their membership
		overdue_days = (getdate(self.return_date) - getdate(self.due_date)).days

        # if overdue days are there calculate the fine based on the membership of the member
		if overdue_days > 0:
			fine = overdue_days * membership_of_member.fine_per_day
			return fine 
		
		return 0  # returning zero if ther is no fine
	

# creating fine doc for the member

	def create_fine(self,fine_amount):

		if frappe.db.exists("Fine", {"book_issue_id":self.name}) :
			return

		fine = frappe.new_doc("Fine")
		fine.book_issue_id = self.name
		fine.late_days = (getdate(self.return_date) - getdate(self.due_date)).days
		fine.fine_amount = fine_amount
		fine.status= "Unpaid"
		fine.insert()
		






		

 

