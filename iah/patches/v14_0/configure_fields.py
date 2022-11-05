import frappe


def execute():
    _make_property_setters()


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
