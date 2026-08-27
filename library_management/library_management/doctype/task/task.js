// Copyright (c) 2026, mano and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Task", {
// 	refresh(frm) {

// 	},
// });

// frappe.call method path libramary_management.api.create_task -> pls check in this
frappe.ui.form.on("Task",{
    refresh(frm){
      frm.add_custom_button(__('Create Task'),()=>{
        let d = new frappe.ui.Dialog({
                title : 'Enter the subject name',
                fields :[{
                    label : 'subject_name',
                    fieldname: 'subject_name',
                    fieldtype : 'Data'
                }],
                primary_action_label: 'createTask',
                primary_action(values){
                    frappe.call({
                        method : 'library_management.api.create_task',
                        args:{
                            subject_name : values.subject_name
                        },
                        callback:function(r){
                           frappe.msgprint({
                            title : 'Success',
                            message: `Task <b>${r.message}</b> created successfully.`,
                            indicator: 'green'
                           })
                        }
                    })
                    d.hide()
                }
            })
            d.show()
        })
    }

})


 