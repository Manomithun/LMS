# Copyright (c) 2026, mano and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document


class Meeting(Document):
	def after_insert(self):
		frappe.enqueue(
        "library_management.api.create_google_event",
        meeting_name=self.name,
        queue="short"
    )
