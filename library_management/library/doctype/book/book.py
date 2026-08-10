# Copyright (c) 2026, mano and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document
import frappe
from frappe.model.document import Document
from datetime import datetime

class Book(Document):

	def validate(self):
		#Getting current date and time
		current_year=datetime.now().year

        #validating the published year to avoid adding future published year
		if self.published_year > current_year:
			frappe.throw("published Year cannot be in future")

	def before_save(self):
		self.book_title=self.book_title.strip()

	def refresh_book_statistics(self):

		self.total_copies = frappe.db.count("BookCopy",{
			"book_id": self.name
		})

		self.avaliable_copies = frappe.db.count("BookCopy",{
			"book_id" : self.name,
			"status"  : "Available"
		})

		self.save()
	

