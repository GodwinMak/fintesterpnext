# # Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# # For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class BorrowerGroup(Document):
    # pass
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from erpnext.selling.doctype.enterprise_group.enterprise_group import EnterpriseGroup
        from erpnext.selling.doctype.group_members.group_members import GroupMembers
        from frappe.types import DF

        chairperson: DF.Link | None
        day_of_the_month: DF.Literal["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
        day_of_week: DF.Literal["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        enterprise_groups: DF.Table[EnterpriseGroup]
        group_members: DF.Table[GroupMembers]
        group_name: DF.Data
        group_type: DF.Literal["Grameen Group Lending", "Other Group Lending"]
        is_eligible_for_loan: DF.Check
        is_parent: DF.Check
        max_members_per_subgroup: DF.Int
        max_total_members: DF.Int
        min_members_per_subgroup: DF.Int
        min_required_members: DF.Int
        min_required_subgroups: DF.Int
        parent_borrower_group: DF.Link | None
        repayment_method: DF.Literal["", "Repay Redusing Amount Over Number per Period", "Repay Fixed Amount Over Number of Periods"]
        repayment_schedule_type: DF.Literal["", "Monthly", "Weekly", "Quarterly"]
        secretary: DF.Link | None
        status: DF.Literal["", "Active", "Inactive"]
        total_members: DF.Int
        total_subgroups: DF.Int
        treasurer: DF.Link | None
    # end: auto-generated types
    # Begin: auto-generated types
    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from erpnext.selling.doctype.enterprise_group.enterprise_group import EnterpriseGroup
        from erpnext.selling.doctype.group_members.group_members import GroupMembers
        from frappe.types import DF

        chairperson: DF.Link | None
        day_of_the_month: DF.Literal[
            "", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", 
            "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", 
            "30", "31"
        ]
        day_of_week: DF.Literal["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        enterprise_groups: DF.Table[EnterpriseGroup]
        group_members: DF.Table[GroupMembers]
        group_name: DF.Data
        group_type: DF.Literal["Grameen Group Lending", "Other Group Lending"]
        is_eligible_for_loan: DF.Check
        is_parent: DF.Check
        max_members_per_subgroup: DF.Int
        max_total_members: DF.Int
        min_members_per_subgroup: DF.Int
        min_required_members: DF.Int
        min_required_subgroups: DF.Int
        parent_borrower_group: DF.Link | None
        repayment_method: DF.Literal[
            "", "Repay Redusing Amount Over Number per Period", "Repay Fixed Amount Over Number of Periods"
        ]
        repayment_schedule_type: DF.Literal["", "Monthly", "Weekly", "Quarterly"]
        secretary: DF.Link | None
        status: DF.Literal["", "Active", "Inactive"]
        total_members: DF.Int
        total_subgroups: DF.Int
        treasurer: DF.Link | None
    # End: auto-generated types

    def validate(self):
        print("hello")
        self.autoname()
#         self.before_insert()  
        
#         if self.is_parent or self.group_type == "Other Group Lending":
#             self.update_group_eligibility()

    def autoname(self):
        """Automatically set the name of the document based on group_name and group_type."""
        print("hello")
        if not self.group_name:
            frappe.throw(_("Group Name is required to set the name."))

        # Strip any extra spaces from the group name
        group_name = self.group_name.strip()

        # Determine the suffix based on group_type and is_parent
        if self.group_type == "Grameen Group Lending":
            suffix = "UMOJA CENTER" if self.is_parent else "ENTERPRISE GROUP"
        elif self.group_type == "Other Group Lending":
            suffix = "GROUP LENDING"
        else:
            suffix = ""  # Default case (if needed)

        # Construct the name
        self.name = f"{group_name} - {suffix}"

    # def before_insert(self):
        # if self.group_type == "Grameen Group Lending":
            # parent_group = frappe.get_doc("Borrower Group", self.parent_borrower_group)
            # print(parent_group)

#             # Ensure total members do not exceed 30
#             if parent_group.total_members >= 30:
#                 frappe.throw(_("Cannot add more members. Maximum limit of 30 reached."))

#             # Ensure subgroup does not exceed 6 members
#             subgroup = frappe.get_doc("Borrower Group", self.enterprise_groups)
#             if subgroup.subgroup_members_count >= 6:
#                 frappe.throw(_("Cannot add more than 6 members in a subgroup."))

#         elif self.group_type == "Other Group Lending":
#             group = frappe.get_doc("Borrower Group", self.name)

#             # Ensure total members do not exceed max limit (optional)
#             if group.total_members >= 30:  # Example max limit
#                 frappe.throw(_("Cannot add more members. Maximum limit of 50 reached."))
    
    
    def update_group_eligibility(self):  # sourcery skip: extract-method
        group = frappe.get_doc("Borrower Group", self.name)  # Use "Borrower Group" for both types

        if self.group_type == "Grameen Group Lending":
            # Fetch subgroups where this group is the parent
            subgroups = frappe.get_all(
                "Borrower Group",
                filters={"parent_borrower_group": self.group_name},
                fields=["name", "total_members"]
            )

            # Calculate total members and total subgroups
            total_members = sum(sub["total_members"] for sub in subgroups)
            total_subgroups = len(subgroups)

            # Update group fields
            group.total_members = total_members
            group.total_subgroups = total_subgroups

            # Eligibility: At least 2 subgroups, each with at least 5 members, and total members ≥ 10
            valid_subgroups = [sub for sub in subgroups if sub["total_members"] >= 5]
            group.is_eligible_for_loan = len(valid_subgroups) >= 2 and total_members >= 10

        elif self.group_type == "Other Group Lending":
            # Count members directly linked to this group
            total_members = frappe.db.count("Borrower", {"borrower_group": self.name})
            
            print(total_members)

            # Eligibility: At least 10 members
            group.is_eligible_for_loan = total_members >= 10
            self.total_members = total_members


@frappe.whitelist()
def get_filtered_borrowers(doctype, txt, searchfield, start, page_len, filters):
    """
    Fetch borrowers who belong to the selected group (either as a parent or as a child group).
    """

    group = filters.get("group")

    if not group:
        return frappe.db.sql(
            """
            SELECT name FROM `tabBorrower`
            WHERE borrower_group = %s
        """,
            (filters.get('group'),),
        )
    # Scenario 1: If the current Borrower group is a parent group (Grameen group)
    child_groups = frappe.get_all("Borrower Group", filters={"parent_borrower_group": group}, pluck="name")

    if child_groups:
        return frappe.db.sql(
            """
            SELECT name FROM `tabBorrower`
            WHERE borrower_group IN ({})
        """.format(
                ", ".join(["%s"] * len(child_groups))
            ),
            tuple(child_groups),
        )
    return frappe.db.sql(
        """
        SELECT name FROM `tabBorrower`
        WHERE borrower_group = %s
    """,
        (group,),
    )


@frappe.whitelist()
def fill_group_members(group_name):
    """
    Automatically fill the 'Group Members' table in child groups and 'Other Group Lending'
    with all borrowers that have the given group_name.
    """

    if not group_name:
        return {"error": "Group Name is required."}

    # Get all borrowers in the specified group
    borrowers = frappe.get_all("Borrower", filters={"borrower_group": group_name}, fields=["full_name"])

    if not borrowers:
        return []

    # Get all child groups with the same group name
    child_groups = frappe.get_all("Borrower Group", filters={"name": group_name}, fields=["name"])

    for group in child_groups:
        group_doc = frappe.get_doc("Borrower Group", group["name"])

        # Clear existing members to avoid duplicates
        group_doc.group_members = []

        # Add all borrowers to the 'Group Members' table
        for borrower in borrowers:
            group_doc.append("group_members", {
                "group_member_name": borrower["full_name"]
            })

        # Save the updated group
        group_doc.save()



@frappe.whitelist()
def get_child_groups(parent_group):
    """
    Fetch all child groups of a given parent Borrower Group.
    """
    if not parent_group:
        return []

    return frappe.get_all(
        "Borrower Group",
        filters={"parent_borrower_group": parent_group},
        fields=["name"],
    )
