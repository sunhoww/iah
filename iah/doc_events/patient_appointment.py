import frappe


def before_save(doc, _):
    dob = frappe.db.get_value("Patient", doc.patient, "dob")

    if dob:
        days = frappe.utils.date_diff(doc.appointment_date, dob)
        if years := int(days / 365):
            doc.patient_age = f"{years} year(s)"
        elif months := int(days / 30):
            doc.patient_age = f"{months} month(s)"
        else:
            doc.patient_age = f"{days} day(s)"
