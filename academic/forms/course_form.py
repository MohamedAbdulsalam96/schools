from django import forms
from academic.models import Course

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = [
			"course",
			"department",
		]
