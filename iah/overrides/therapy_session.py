from healthcare.healthcare.doctype.therapy_session.therapy_session import (
    TherapySession as Standard,
)


class TherapySession(Standard):
    def on_submit(self):
        pass

    def on_cancel(self):
        pass

    def update_sessions_count_in_therapy_plan(self, on_cancel=False):
        if self.therapy_plan:
            super().update_sessions_count_in_therapy_plan(on_cancel=on_cancel)
