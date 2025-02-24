// Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Borrower", {
	refresh(frm) {

	},
    setup: function(frm) {
        frm.set_query("borrower_group", function() {
            return {
                filters: [
                    ["Borrower Group", "is_parent", "=", 0],
                    ["Borrower Group", "group_type", "in", ["Grameen Group Lending", "Other Group Lending"]]
                ]
            };
        });
    }
});
