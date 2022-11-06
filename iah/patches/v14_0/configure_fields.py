import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field


def execute():
    _make_custom_fields()
    _make_property_setters()


def _make_custom_fields():
    fixtures = {
        "Patient Appointment": [
            {
                "label": "Ref Patient Appointment",
                "fieldname": "ref_patient_appointment",
                "fieldtype": "Link",
                "options": "Patient Appointment",
                "insert_after": "status",
                "set_only_once": 1,
                "no_copy": 1,
            }
        ]
    }
    for doctype, docfields in fixtures.items():
        for df in docfields:
            create_custom_field(doctype, df)


def _make_property_setters():
    fixtures = {
        "Patient Appointment": [
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
        ],
        "Therapy Session": [
            {
                "fieldname": "therapy_plan",
                "property": "reqd",
                "property_type": "Check",
                "value": 0,
            },
            {
                "fieldname": "therapy_plan",
                "property": "hidden",
                "property_type": "Check",
                "value": 1,
            },
            {
                "fieldname": "therapy_type",
                "property": "depends_on",
                "property_type": "Data",
                "value": "",
            },
        ],
    }
    for doctype, docfields in fixtures.items():
        for kwargs in docfields:
            args = {"doctype": doctype, "doctype_or_field": "DocField", **kwargs}
            frappe.make_property_setter(args)
