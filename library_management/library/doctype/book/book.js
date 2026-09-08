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
        frappe.msgprint(__("Welcome to the Book Form! Please fill in the details below."));
        // console.log(frappe.session.user)
        // console.log(frappe.csrf_token)
        
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


        if (frm.is_new()) {

    let dai = new frappe.ui.Dialog({
        title: 'Enter the Book Details',

        fields: [
            {
                label: 'Title',
                fieldname: 'title',
                fieldtype: 'Data'
            },
            {
                label: 'ISBN',
                fieldname: 'isbn',
                fieldtype: 'Data'
            }
        ],

        primary_action_label: 'Submit',

        primary_action(values) {
            frm.set_value('book_title', values.title);
            frm.set_value('isbn', values.isbn);

            dai.hide();
        }
    });

    dai.show();
}
    },
    after_save(frm){
        frappe.utils.play_sound("ping")
    }
    
})