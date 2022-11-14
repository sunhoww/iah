from . import __version__ as app_version

app_name = "iah"
app_title = "IAH"
app_publisher = "Libermatic"
app_description = "Customizations for IAH"
app_email = "info@libermatic.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/iah/css/iah.css"
# app_include_js = "/assets/iah/js/iah.js"

# include js, css files in header of web template
# web_include_css = "/assets/iah/css/iah.css"
# web_include_js = "/assets/iah/js/iah.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "iah/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Patient Appointment": "public/js/client_script/patient_appointment.js",
    "Stock Entry": "public/js/client_script/stock_entry.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "iah.utils.jinja_methods",
# 	"filters": "iah.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "iah.install.before_install"
# after_install = "iah.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "iah.uninstall.before_uninstall"
# after_uninstall = "iah.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "iah.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
    "Asset": "iah.overrides.asset.Asset",
    "Patient Appointment": "iah.overrides.patient_appointment.PatientAppointment",
    "Therapy Session": "iah.overrides.therapy_session.TherapySession",
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Asset": {"before_insert": "iah.doc_events.asset.before_insert"},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"iah.tasks.all"
# 	],
# 	"daily": [
# 		"iah.tasks.daily"
# 	],
# 	"hourly": [
# 		"iah.tasks.hourly"
# 	],
# 	"weekly": [
# 		"iah.tasks.weekly"
# 	],
# 	"monthly": [
# 		"iah.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "iah.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "iah.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "iah.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"iah.auth.validate"
# ]
