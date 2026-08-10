import frappe

@frappe.whitelist()
def getBookList():
    Book = frappe.qb.DocType("Book")
    BookCopy = frappe.qb.DocType("BookCopy")
    query = frappe.qb.from_(Book).join(BookCopy).on(Book.name == BookCopy.book_id).select(Book.name,Book.book_title,BookCopy.status)
    records = query.run(as_dict = True)
    if not records:
        return []
    doc = frappe.get_doc("Book", records[0]["name"])
    
    doc.book_title = "Testing"
    doc.save()

    for record in records:
        frappe.db.set_value(
            "Book",
            record["name"],
            "published_year",
            2026
        )
    return records