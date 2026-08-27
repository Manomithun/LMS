import frappe

def execute():
    users = frappe.get_all(
        "Member",
        fields=["name","email"]
    )

    for user in users:
        user_type = "Registered" if user.email else "Guest" 

        frappe.db.set_value(
            "Member",
            user.name,
            "user_type",
            user_type
        )