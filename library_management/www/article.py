import frappe

def get_context(context):
    context.articles = frappe.get_all(
        "article",
        fields=["name", "title","status"]
    )