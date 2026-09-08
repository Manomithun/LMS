console.log("Library Management JS loadedd");
frappe.ui.form.on("Book",{
    refresh(frm){
        frappe.msgprint("Book Form Refreshed");
    }
});