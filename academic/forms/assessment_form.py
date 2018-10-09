from django import forms
from academic.models import Assessment

class AssessmentForm(forms.ModelForm):
	class Meta:
		model = Assessment
		fields = [
			"student",
			"exam",
			"subject",
			"marks_scored",
		]
