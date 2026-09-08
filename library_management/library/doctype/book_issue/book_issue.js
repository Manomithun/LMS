// Copyright (c) 2026, mano and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Book Issue", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Book Issue",{
    setup(frm){
        frm.set_query("copyid",function(){
            return{
            query : "library_management.api.get_book_copy_filter"

            }
        })
    },
    onload(frm){
        // frappe.msgprint("Hi from oneload")
    },
    refresh(frm){
        frm.add_custom_button("View Member",()=>{
            if(frm.doc.member){
                frappe.set_route("Form","Member",frm.doc.member);
            }
        },"View");
        frm.add_custom_button("View BookCopy",()=>{
            if(frm.doc.copyid){
                frappe.set_route("Form","BookCopy",frm.doc.copyid)
            }
        },"View")
    }
})