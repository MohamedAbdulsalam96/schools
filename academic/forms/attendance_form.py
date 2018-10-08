from django import forms
from academic.models import Attendance

class AttendanceForm(forms.ModelForm):
	class Meta:
		model = Attendance
		fields = [
			"student",
			"attendance_date",
			"attendance",
		]
