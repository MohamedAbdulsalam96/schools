from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
	# fields in the Parent Model
	user = models.OneToOneField(User, default=None)
	title = models.CharField(max_length=100)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	# contact details
	mobile = models.CharField(max_length=10)

	assigned_class = models.ForeignKey('Standard')
	assigned_division = models.ForeignKey('Division')
	# assigned_subject = models.ForeignKey('Subject')

	def __str__(self):
		return self.title
