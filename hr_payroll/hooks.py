# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "hr_payroll"
app_title = "Hr Payroll"
app_publisher = "patil"
app_description = "HR"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "patil.sangram01@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hr_payroll/css/hr_payroll.css"
# app_include_js = "/assets/hr_payroll/js/hr_payroll.js"

# include js, css files in header of web template
# web_include_css = "/assets/hr_payroll/css/hr_payroll.css"
# web_include_js = "/assets/hr_payroll/js/hr_payroll.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "hr_payroll.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "hr_payroll.install.before_install"
# after_install = "hr_payroll.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hr_payroll.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hr_payroll.tasks.all"
# 	],
# 	"daily": [
# 		"hr_payroll.tasks.daily"
# 	],
# 	"hourly": [
# 		"hr_payroll.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hr_payroll.tasks.weekly"
# 	]
# 	"monthly": [
# 		"hr_payroll.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "hr_payroll.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hr_payroll.event.get_events"
# }

