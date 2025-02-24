// Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Borrower Group", {
	refresh(frm) {
        // frm.fields_dict["group_members"].grid.get_field("borrower").get_query = function(doc, cdt, cdn) {
        //     return {
        //         filters: {
        //             borrower_group: doc.name  // Show only borrowers in this group
        //         }
        //     };
        // };
    },
	// setup: function (frm) {
    //     if (frm.doc.is_parent) {
    //         frappe.call({
    //             method: "erpnext.selling.doctype.borrower_group.borrower_group.get_child_groups",
    //             args: { parent_group: frm.doc.name },
    //             callback: function(r) {
    //                 if (r.message) {
    //                     frm.clear_table("enterprise_groups");  // Clear existing table entries
    //                     r.message.forEach(child => {
    //                         let row = frm.add_child("enterprise_groups");
    //                         row.enterprise_group_name = child.name;  // Set child group name
    //                     });
    //                     frm.refresh_field("enterprise_groups");
    //                 }
    //             }
    //         });
    //     }
	// 	if (frm.doc.group_name) {
	// 		["chairperson", "treasurer", "secretary"].forEach((field) => {
	// 			frm.set_query(field, function () {
	// 				return {
	// 					query: "erpnext.selling.doctype.borrower_group.borrower_group.get_filtered_borrowers",
	// 					filters: {
	// 						group: frm.doc.is_parent
	// 							? frm.doc.name
	// 							: frm.doc.parent_borrower_group || frm.doc.name,
	// 					},
	// 				};
	// 			});
	// 		});
	// 	}
    //     if (frm.doc.group_name) {
    //         frappe.call({
    //             method: "erpnext.selling.doctype.borrower_group.borrower_group.fill_group_members",
    //             args: { group_name: frm.doc.name },
    //             callback: function(response) {
    //                 if (response.message) {
    //                     frappe.msgprint(response.message);
    //                     frm.reload_doc();  // Reload the document to reflect changes
    //                 }
    //             }
    //         });
    //     }
        
	// },
    // group_name: function(frm) {
    //     // Refresh the borrower field filter when group_name changes
    //     frm.fields_dict["group_members"].grid.get_field("borrower").get_query = function(doc, cdt, cdn) {
    //         return {
    //             filters: {
    //                 borrower_group: doc.name
    //             }
    //         };
    //     };
    // },
});
