import frappe
from healthcare.healthcare.doctype.patient_appointment.patient_appointment import (
    PatientAppointment as Standard,
)
from healthcare.healthcare.doctype.healthcare_settings.healthcare_settings import (
    get_appointment_item,
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
        if not self.appointment_type:
            return

        super().set_payment_details()


def _invoice_appointment(appointment_doc):
    if not appointment_doc.appointment_type:
        return

    sales_invoice = frappe.new_doc("Sales Invoice")
    sales_invoice.patient = appointment_doc.patient
    sales_invoice.customer = frappe.get_value(
        "Patient", appointment_doc.patient, "customer"
    )
    sales_invoice.appointment = appointment_doc.name
    sales_invoice.set_posting_time = 1
    sales_invoice.posting_date = appointment_doc.appointment_date
    sales_invoice.due_date = frappe.utils.getdate()
    sales_invoice.company = appointment_doc.company
    sales_invoice.debit_to = get_receivable_account(appointment_doc.company)

    item = sales_invoice.append("items", {})
    item = get_appointment_item(appointment_doc, item)

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
        {
            "invoiced": 1,
            "ref_sales_invoice": sales_invoice.name,
        },
    )
