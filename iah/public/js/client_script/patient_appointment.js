frappe.ui.form.on('Patient Appointment', {
  setup: function (frm) {
    frm.set_query('therapy_type', ({ department }) => ({
      filters: { medical_department: department },
    }));
    frm.set_query('ref_patient_appointment', () => ({
      filters: { therapy_type: ['is', 'set'] },
    }));
  },
  refresh: function (frm) {
    if (
      frm.doc.status == 'Open' ||
      (frm.doc.status == 'Scheduled' && !frm.doc.__islocal)
    ) {
      if (frm.doc.appointment_type) {
        frm.add_custom_button(
          'Therapy Appointment',
          () => {
            const { name: ref_patient_appointment, patient } = frm.doc;
            frappe.new_doc('Patient Appointment', {
              ref_patient_appointment,
              patient,
            });
          },
          __('Create')
        );
      }
    }
  },
  ref_patient_appointment: async function (frm) {
    const { ref_patient_appointment } = frm.doc;
    if (ref_patient_appointment) {
      const { message: doc } = await frappe.db.get_value(
        'Patient Appointment',
        ref_patient_appointment,
        ['patient']
      );
      frm.set_value('patient', doc?.patient);
    }
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
