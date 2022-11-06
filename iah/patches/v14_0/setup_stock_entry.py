import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field


def execute():
    frappe.get_doc(
        {
            "doctype": "Stock Entry Type",
            "name": "Dispensary Issue",
            "purpose": "Material Issue",
        }
    ).insert(ignore_if_duplicate=True)

    _make_custom_fields()


def _make_custom_fields():
    docfields = [
        {
            "label": "Patient Appointment",
            "fieldname": "patient_appointment",
            "fieldtype": "Link",
            "options": "Patient Appointment",
            "no_copy": 1,
            "depends_on": "eval:doc.stock_entry_type === 'Dispensary Issue'",
            "mandatory_depends_on": "eval:doc.stock_entry_type === 'Dispensary Issue'",
            "insert_after": "add_to_transit",
        }
    ]
    for df in docfields:
        create_custom_field("Stock Entry", df)
