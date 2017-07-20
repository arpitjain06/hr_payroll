frappe.pages['admin-dashboard'].on_page_load = function(wrapper) {
	new frappe.AdminDashboard({
		$wrapper: $(wrapper)
	});
	frappe.breadcrumbs.add("HR");
}

frappe.AdminDashboard = Class.extend({
	init: function(opts) {
		this.$wrapper = opts.$wrapper
		this.render_layout();
	},
	render_layout: function() {
		this.$wrapper.empty();
		var me = this;
		frappe.call({
			method: "hr_payroll.hr_payroll.page.admin_dashboard.admin_dashboard.get_hr_master_count",
			callback: function(r) {
				me.$wrapper.append(frappe.render_template("admin_dashboard", {'data': r.message}));
				me.render_charts();
				me.render_employee_list();
				me.active_treeview();
				me.render_dashboard();
			}
		})
	},

	render_charts: function() {
		$("#piechart").css({"width":"400px","height":"200px"})
		$("#splinechart").css({"width":"400px","height":"200px"})
		var chart = c3.generate({
			bindto: '#piechart',
			data: {
				// iris data from R
				columns: [
					['dataa', 30],
					['datab', 40],
					['datac', 50],
					['datad', 100],
				],
				type : 'pie',
			}
		});

		var chart = c3.generate({
			bindto: "#splinechart",
			data: {
				columns: [
					['data1', 300, 350, 300, 0, 0, 120],
					['data2', 130, 100, 140, 200, 150, 50]
				],
				types: {
					data1: 'area-spline',
					data2: 'area-spline'
					// 'line', 'spline', 'step', 'area', 'area-step' are also available to stack
				},
				groups: [['data1', 'data2']]
			}
		});
	},

	active_treeview: function() {
		var me = this;
		$('.active_tree').click(function() {
			console.log("Yeahhh")
			$('.treeview').toggleClass('active');
		})
	},

	render_employee_list: function() {
		var me = this;
		$('#employee_list').click(function() {
			frappe.call({

				method: "hr_payroll.hr_payroll.page.admin_dashboard.admin_dashboard.get_employee_list",
				callback: function(r) {
					$('.admin-content').empty();
					$('.admin-content').append(frappe.render_template("employee_list", {'data': r.message}));
				}
			})
		})
	},

	render_dashboard: function() {
		var me = this;
		$('#dashboard').click(function() {
			me.render_layout()
		})
	}
})
