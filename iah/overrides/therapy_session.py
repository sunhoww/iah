from healthcare.healthcare.doctype.therapy_session.therapy_session import (
    TherapySession as Standard,
)


class TherapySession(Standard):
    def update_sessions_count_in_therapy_plan(self, on_cancel=False):
        if self.therapy_plan:
            super().update_sessions_count_in_therapy_plan(on_cancel=on_cancel)
