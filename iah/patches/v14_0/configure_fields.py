import frappe


def execute():
    _make_property_setters()


def _make_property_setters():
    fixtures = {
        "Patient Appointment": [
            ("therapy_plan", "hidden", 1),
            ("therapy_type", "label", "Therapy Type"),
            ("therapy_type", "depends_on", "eval:doc.patient;"),
        ],
        "Therapy Session": [
            ("therapy_plan", "reqd", 0),
            ("therapy_plan", "hidden", 0),
            ("therapy_type", "depends_on", ""),
        ],
    }
    for doctype, docfields in fixtures.items():
        for fieldname, property, value in docfields:
            frappe.make_property_setter(
                {
                    "doctype": doctype,
                    "doctype_or_field": "DocField",
                    "fieldname": fieldname,
                    "property": property,
                    "value": value,
                }
            )
