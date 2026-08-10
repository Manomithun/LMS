# Copyright (c) 2026, mano and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Category(Document):

	def before_save(self):

		#clean and update the category name
		self.category=self.category.strip()
		frappe.msgprint("Category Saved Successfully")
