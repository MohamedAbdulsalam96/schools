from django import forms
from profiles.models import Parent

class ParentForm(forms.ModelForm):
	class Meta:
		model = Parent
		fields = [
			"first_name",
			"last_name",
			"user",
			"mobile",
		]
