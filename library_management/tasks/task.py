import frappe

def excute():
    books = frappe.get_all("Book", filters = {
        "status" :"Approve",
        "due_date" : ["<", frappe.utils.today()]
    },
    pluck= "name")
    for book in books:
        frappe.db.set_value("Book",book,"status","OverDue")
    frappe.db.commit()

    import frappe

def execute():
    books = frappe.get_all("Book", filters = {
        "status" :"Approve",
        "due_date" : ["<", frappe.utils.today()]
    },
    pluck= "name")
    for book in books:
        frappe.db.set_value("Book",book,"status","OverDue")
    frappe.db.commit()