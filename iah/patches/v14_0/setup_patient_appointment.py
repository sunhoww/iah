import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field


def execute():
    _make_property_setters()


def _make_property_setters():
    docfields = [
        {
            "fieldname": "therapy_plan",
            "property": "hidden",
            "property_type": "Check",
            "value": 1,
        },
        {
            "fieldname": "therapy_type",
            "property": "label",
            "property_type": "Data",
            "value": "Therapy Type",
        },
        {
            "fieldname": "therapy_type",
            "property": "depends_on",
            "property_type": "Data",
            "value": "eval:doc.patient;",
        },
    ]
    for kwargs in docfields:
        args = {
            "doctype": "Patient Appointment",
            "doctype_or_field": "DocField",
            **kwargs,
        }
        frappe.make_property_setter(args)
