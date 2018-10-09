from django import forms
from academic.models import Subject

class SubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = [
			"subject",
            "course",
            "passing_marks",
            "max_marks"
		]
