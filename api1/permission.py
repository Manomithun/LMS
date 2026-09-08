import frappe
def has_app_permission():
    # return frappe.session.user in ("Administrator",) or ("Library Manager",) in frappe.get_roles() 
    return True