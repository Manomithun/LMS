import frappe

def execute(filters=None):
    columns, data = get_columns(), get_data(filters)
    return columns, data

def get_columns():
    return [
        {
            "label": "Book ID",
            "fieldname": "book_id",
            "fieldtype": "Link",
            "options": "Book",
            "width": 150
        },
        {
            "label": "Tittle",
            "fieldname": "tittle",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Status",
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Condition",
            "fieldname": "condition",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Purchase Date",
            "fieldname": "purchase_date",
            "fieldtype": "Date",
            "width": 120
        }
    ]

def get_data(filters):
    return frappe.db.get_list("BookCopy", filters, ["book_id", "tittle", "status", "condition", "purchase_date"])