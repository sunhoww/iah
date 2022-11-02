import frappe
from erpnext.assets.doctype.asset.asset import Asset as Standard


class Asset(Standard):
    def validate_asset_values(self):
        if not self.asset_category:
            self.asset_category = frappe.get_cached_value(
                "Item", self.item_code, "asset_category"
            )
        
        if not frappe.utils.flt(self.gross_purchase_amount):
            return

        super().validate_asset_values()

    
def before_insert(doc, _):
    if not frappe.utils.flt(doc.gross_purchase_amount):
        doc.calculate_depreciation = 0