// // Copyright (c) 2026, mano and contributors
// // For license information, please see license.txt

// frappe.ui.form.on("Member", {
//     refresh(frm) {

//         console.log("Member:", frm.doc.name);

//         // Don't fetch for a new/unsaved Member
//         if (frm.is_new()) {
//             return;
//         }

//         // Clear previously displayed rows
//         frm.clear_table("books");

//         frappe.db.get_list("Book Issue", {
//             filters: {
//                 member: frm.doc.name
//             }
//         }).then(records => {

//             for (let record of records) {

//                 console.log("Book Issue:", record);

//                 let row = frm.add_child("books");

//                 row.book_issue = record.name;
//                 row.book = record.book;
//                 row.issue_date = record.issue_date;
//                 row.return_date = record.return_date;

//                 console.log("Child row:", row);
//             }

//             frm.refresh_field("books");
//         });
//     }
// });
// frappe.ui.form.on("Book Purchase", {
//     after_save(frm) {
//         frappe.call({
//             method: "library_management.api.add_book_to_member",
//             args: {
//                 member: frm.doc.member,
//                 book: frm.doc.book
//             }
//         });
//     }
// });

frappe.ui.form.on("Member",{
    refresh(frm) {
        // frm.set_df_property("email", "masked", true);
        // frappe.db.get_value("Member", frm.doc.name, "email", (r) => {
        //     if (r && r.email) {
        //         frm.set_df_property("email", "masked", true);
        //     }
        // }); 
        // [name1,domain] = frm.doc.email.split("@")
        // masked = name1.charAt(0) + "***@" + domain
        // frm.set_df_property("email","read_only",1)
        // frm.set_value("email",masked) --> it will change the value and when u submit it ,it gets into db
        frm.set_df_property("email", "masked", true);

    }
});