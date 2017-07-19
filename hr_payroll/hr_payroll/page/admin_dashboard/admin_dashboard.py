import frappe

@frappe.whitelist()
def get_hr_master_count():
	employee = frappe.db.get_value("Employee", {"status": "Active"}, "count(name)")
	user = frappe.db.get_value("User", {"enabled": 1}, "count(name)")
	expense_claim = frappe.db.get_value("Expense Claim", {"approval_status": "Draft"}, "count(name)")
	leave_application = frappe.db.get_value("Leave Application", {"status": "Open"}, "count(name)")
	return {"employee": employee, "user": user, "leave_application": leave_application, "expense_claim": expense_claim}

@frappe.whitelist()
def get_employee_list():
	return frappe.db.sql("""select name, employee_name, date_of_joining, status, user_id from `tabEmployee`""", as_dict=True)