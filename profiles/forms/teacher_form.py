from django import forms
from profiles.models import Teacher

class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = [
			"user",
			"first_name",
			"last_name",
		]
