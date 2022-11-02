import frappe
from healthcare.healthcare.doctype.patient_appointment.patient_appointment import (
    PatientAppointment as Standard,
    invoice_appointment,
)
from healthcare.healthcare.doctype.healthcare_settings.healthcare_settings import (
    get_income_account,
    get_receivable_account,
)


class PatientAppointment(Standard):
    def validate(self):
        super().validate()
        if bool(self.appointment_type) == bool(self.therapy_type):
            frappe.throw(
                "Only one of <em>Appointment Type</em> or <em>Therapy Type</em> is "
                "required."
            )

    def validate_overlaps(self):
        pass

    def after_insert(self):
        # self.update_prescription_details()
        self.set_payment_details()
        _invoice_appointment(self)
        if self.appointment_type:
            self.update_fee_validity()
        # send_confirmation_msg(self)

    def set_payment_details(self):
        if self.appointment_type:
            super().set_payment_details()
            return

        # assuming self.therapy_type is always set when self.appointment_type is not
        if frappe.db.get_single_value(
            "Healthcare Settings", "automate_appointment_invoicing"
        ):
            therapy_type = frappe.get_cached_value(
                "Therapy Type",
                self.therapy_type,
                fieldname=["item", "rate", "is_billable"],
                as_dict=True,
            )
            if not therapy_type:
                frappe.throw(f"Unknown <em>Therapy Type</em>: {self.therapy_type}")

            if therapy_type.is_billable:
                self.db_set("billing_item", therapy_type.item)
                self.db_set("paid_amount", therapy_type.rate)


def _invoice_appointment(appointment_doc):
    if appointment_doc.appointment_type:
        invoice_appointment(appointment_doc)
        return

    therapy_type = frappe.get_cached_value(
        "Therapy Type",
        appointment_doc.therapy_type,
        fieldname=["item", "rate", "is_billable"],
        as_dict=True,
    )
    if not therapy_type:
        frappe.throw(f"Unknown <em>Therapy Type</em>: {appointment_doc.therapy_type}")

    if not therapy_type.is_billable:
        return

    sales_invoice = frappe.new_doc("Sales Invoice")
    sales_invoice.patient = appointment_doc.patient
    sales_invoice.customer = frappe.get_value(
        "Patient", appointment_doc.patient, "customer"
    )
    sales_invoice.appointment = appointment_doc.name
    sales_invoice.due_date = frappe.utils.getdate()
    sales_invoice.company = appointment_doc.company
    sales_invoice.debit_to = get_receivable_account(appointment_doc.company)

    charge = appointment_doc.paid_amount or therapy_type.rate
    sales_invoice.append(
        "items",
        {
            "item_code": therapy_type.item,
            "income_account": get_income_account(
                appointment_doc.practitioner, appointment_doc.company
            ),
            "cost_center": frappe.get_cached_value(
                "Company", appointment_doc.company, "cost_center"
            ),
            "rate": charge,
            "amount": charge,
            "qty": 1,
            "reference_dt": "Patient Appointment",
            "reference_dn": appointment_doc.name,
        },
    )

    # Add payments if payment details are supplied else proceed to create invoice as Unpaid
    if appointment_doc.mode_of_payment and appointment_doc.paid_amount:
        sales_invoice.is_pos = 1
        payment = sales_invoice.append("payments", {})
        payment.mode_of_payment = appointment_doc.mode_of_payment
        payment.amount = appointment_doc.paid_amount

    sales_invoice.set_missing_values(for_validate=True)
    sales_invoice.flags.ignore_mandatory = True
    sales_invoice.save(ignore_permissions=True)
    sales_invoice.submit()
    frappe.msgprint("Sales Invoice {0} created".format(sales_invoice.name), alert=True)
    frappe.db.set_value(
        "Patient Appointment",
        appointment_doc.name,
        {"invoiced": 1, "ref_sales_invoice": sales_invoice.name},
    )
