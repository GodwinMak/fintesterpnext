# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class Borrower(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.contacts.doctype.identification_information.identification_information import IdentificationInformation
        from frappe.types import DF

        borrower_group: DF.Link | None
        borrower_image: DF.AttachImage | None
        borrower_type: DF.Literal["Company", "Individual", "Partnership"]
        district: DF.Data | None
        email_id: DF.Data | None
        employers_physical_address: DF.Data | None
        first_name: DF.Data
        full_name: DF.Data | None
        gender: DF.Link
        identification: DF.Table[IdentificationInformation]
        last_name: DF.Data
        loan_officer: DF.Link | None
        marital_status: DF.Literal["Single", "Married", "Divorced", "Widowed"]
        middle_name: DF.Data | None
        mobile_number: DF.Data | None
        region: DF.Data | None
        residence_type: DF.Literal["Rented", "Owned"]
        status: DF.Literal["Active", "Inactive"]
        street: DF.Data | None
        ward: DF.Data | None
        work_place: DF.Data | None
    # end: auto-generated types

    def validate(self):
        self.set_borrower_name()  # Set full name before saving
        self.autoname()  # Trigger autoname logic
  
    def autoname(self):
        # Ensure full name is set before assigning to name
        print("Setting name to:", self.full_name)
        self.name = self.full_name
        print("Name is now:", self.name)
  
    def set_borrower_name(self):
        # Concatenate first, middle, and last names to form full name
        self.full_name = " ".join(
            filter(lambda x: x, [self.first_name, self.middle_name, self.last_name])
        )

@frappe.whitelist()
def fetch_repayment_info(borrower_name):
    """
    Fetch repayment info for a borrower from their Borrower Group.
    """
    try:
        # Fetch the Borrower document
        borrower = frappe.get_doc("Borrower", borrower_name)


        # Ensure the Borrower has a linked Borrower Group
        if not borrower.borrower_group:
            # return {"error": _("Borrower '{0}' does not belong to any Borrower Group.").format(borrower_name)}
            return

        # Fetch the group details
        borrower_group = frappe.get_doc("Borrower Group", borrower.borrower_group)


        # Check for a parent group
        parent_group_name = borrower_group.parent_borrower_group or borrower_group.name
        print(parent_group_name)

        parent_group = frappe.get_doc("Borrower Group", parent_group_name)

        return {
            "repayment_schedule_type": parent_group.repayment_schedule_type,
            "day_of_week": parent_group.day_of_week,
            "day_of_the_month": parent_group.day_of_the_month,
            "repayment_method": parent_group.repayment_method,
            "repayment_periods": parent_group.repayment_periods,
        }
    except frappe.DoesNotExistError:
        return {"error": _("Borrower or Borrower Group does not exist.")}
    except Exception as e:
        frappe.log_error(message=str(e), title="Repayment Info Fetch Error")
        return {"error": _("An unexpected error occurred. Please check the logs.")}