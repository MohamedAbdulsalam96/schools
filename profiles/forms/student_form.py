from django import forms
from profiles.models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = [
			"user",
			"first_name",
			"last_name",
			"date_of_joining",
			"roll_no",
			"course",
			"department",
			"created_by"
		]
