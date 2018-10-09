from django import forms
from academic.models import Exam

class ExamForm(forms.ModelForm):
	class Meta:
		model = Exam
		fields = [
			"exam",
			"exam_date",
		]
