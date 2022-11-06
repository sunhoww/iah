frappe.ui.form.on('Patient Appointment', {
  setup: function (frm) {
    frm.set_query('therapy_type', ({ department }) => ({
      filters: { medical_department: department },
    }));
  },
  therapy_type: async function (frm) {
    const { therapy_type, invoiced } = frm.doc;
    if (!invoiced) {
      if (therapy_type) {
        const { message: doc } = await frappe.db.get_value(
          'Therapy Type',
          therapy_type,
          ['rate']
        );
        frm.set_value('paid_amount', doc?.rate);
      } else {
        frm.set_value('paid_amount', null);
      }
    }
  },
});
