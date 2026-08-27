// Copyright (c) 2026, mano and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Book", {
// 	refresh(frm) {

// 	},
// });

frappe.realtime.on("status_changed",(data)=>{
    console.log(data)
})

frappe.ui.form.on("Book",{
    refresh(frm){
        if(frappe.perm.has_perm(frm.doctype,0,"Approve",frm.doc.name)){
            frm.add_custom_button(__('Approve'),()=>{
                frappe.call({
                    "method": "library_management.api.Approve_book",
                    "args" :{
                        book_id: frm.doc.name
                    },
                    callback: function(r){
                        console.log(r.message)
                        frm.reload_doc()
                    }
                })
            })
        }

        if(frappe.perm.has_perm(frm.doctype,0,"Approve",frm.doc.name)){
            frm.add_custom_button(__('Reject'),()=>{
                frappe.call({
                    "method": "library_management.api.Reject_book",
                    "args" :{
                        book_id : frm.doc.name
                    },
                    "callback" :function(r){
                        console.log(r.message)
                        frm.reload_doc()
                    }

                })
            })
        }

    }
    
})