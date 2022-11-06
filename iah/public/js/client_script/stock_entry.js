frappe.ui.form.on('Stock Entry', {
  setup: function (frm) {
    frm.set_query('patient_appointment', () => ({
      filters: { appointment_type: ['is', 'set'] },
    }));
  },
});
