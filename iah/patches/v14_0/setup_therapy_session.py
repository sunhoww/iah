import frappe


def execute():
    _make_property_setters()


def _make_property_setters():
    docfields = [
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
    ]
    for kwargs in docfields:
        args = {
            "doctype": "Therapy Session",
            "doctype_or_field": "DocField",
            **kwargs,
        }
        frappe.make_property_setter(args)
