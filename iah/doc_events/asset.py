import frappe


def before_insert(doc, _):
    if not frappe.utils.flt(doc.gross_purchase_amount):
        doc.calculate_depreciation = 0
