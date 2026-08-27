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


@frappe.whitelist()
def get_library_status():
    bookCount = frappe.db.count("Book")
    members  = frappe.db.count("Member")
    BookIssued = frappe.db.count("Book Issue", {
        "status" : "Issued"
    })
    available_books = bookCount - BookIssued
    frappe.msgprint(f"Total Books: {bookCount}, Total Members: {members}, Book Issued: {BookIssued}, Available Books: {available_books}")

    return {
        "Total_Books" : bookCount,
        "Total_Members" : members,
        "Book_Issued" : BookIssued,
        "Available_book" : available_books
    }


@frappe.whitelist()
def Approve_book(book_id):
    book = frappe.get_doc("Book",book_id)

    if(not frappe.has_permission(book,"Approve")):
        frappe.throw("You are not premitted to approve",frappe.PermissionError)

    book.status = "Approve"
    book.save()
    return 1

@frappe.whitelist()
def Reject_book(book_id,):
    book = frappe.get_doc("Book",book_id)
    if(not frappe.has_permission(book,"Reject")):
            frappe.throw("You are not premitted to Reject",frappe.PermissionError)
    
    book.status = "Reject"
    book.save()
    return 2



def custom_logic(doc, method):
    frappe.msgprint("Hook executed!")

