# Copyright (c) 2026, mano and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate, nowdate
class BookCopy(Document):

	def after_insert(self):
		book = frappe.get_doc("Book",self.book_id)
		book.refresh_book_statistics()

	def on_trash(self):
		book = frappe.get_doc("Book",self.book_id)
		book.refresh_book_statistics()
		

	def validate(self):
		
		purchase_date=getdate(self.purchase_date)

		today=getdate(nowdate())

		#Validating purchase_date to avoid entring future date
		if purchase_date > today :
			frappe.throw("Invalid purchase_date")
