# Copyright (c) 2026, mano and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Author(Document):
	def before_save(self):
		# clean and update the author name
		self.author_name=self.author_name.strip()

		
		frappe.msgprint("Author data saved successfully")
