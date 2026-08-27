import re
import frappe
from frappe.core.doctype.user.user import cached_property
from frappe.model.document import Document
from library_management.enums import MembersType
from frappe.utils import getdate,nowdate
class Member(Document):
    @cached_property
    def member_book(self):
        books = frappe.get_all(
            "Book Issue",
            filters={
                "member": self.name
            },
            fields=[
                "copyid",
                "due_date"
            ]
        )
        return [
            {
                "bookcopy": row.copyid,
                "duedate": row.due_date
            }
            for row in books
        ]
    
    def validate(self):
        # Get the linked MemberShip document
        membership = frappe.get_doc("MemberShip", self.membertype)

        # Clean the roll number
        roll = (self.rollnumber or "").strip()
        self.rollnumber = roll  # Update the roll number after stripping whitespace

		#Clean the name of the Member
        name1=self.name1.strip()
        self.name1=name1 #Update the roll number after stripping Whitespace

        # Student: 23CSB05 (2 digits + 3 letters + 2 or 3 digits)
        patternST = r"^\d{2}[A-Za-z]{3}\d{2,3}$"

        # Faculty: CSE001 or IT123 (2-4 letters + 3 or more digits)
        patternF = r"^[A-Za-z]{2,4}\d{3,}$"

        # Validate based on member type 
        if membership.member_type == MembersType.STUDENT.value:
            if not re.fullmatch(patternST, roll): 
                frappe.throw(
                    "Invalid Student Roll Number.\n"
                    "Example: 23CSB05"
                )

        elif membership.member_type == MembersType.FACULTY.value:
            if not re.fullmatch(patternF, roll):
                frappe.throw(
                    "Invalid Faculty ID.\n"
                    "Example: CSE001"
                )

		#validating the joindate of the user to avoid entering the future joining date
        today=getdate(nowdate())
        
        if getdate(self.join_date) > today :
            frappe.throw("Invalid Joining Date-> Entering Future date")
             

    def before_save(self):
        frappe.msgprint("Member saved successfully.")