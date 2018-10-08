from __future__ import unicode_literals

from django.db import models
from schools.settings import AUTH_USER_MODEL
from django.db.models.signals import pre_save

class Parent(models.Model):
	# fields in the Parent Model
	user = models.OneToOneField(AUTH_USER_MODEL, default=None)
	title = models.CharField(max_length=100)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	# contact details
	mobile = models.CharField(max_length=10)

	def __str__(self):
		return self.title or "{0} {1}".format(self.first_name, self.last_name)

def validate(sender, instance=None, **kwargs):
	"""
		set the values to fields and validate the Parent information raise the
		error if any
		# set title for the parent before save
	"""

	instance.title = " ".join([instance.first_name, instance.last_name])
	# ToDo get the current logged in user

pre_save.connect(validate, sender=Parent)

class ParentItem(models.Model):

	parent = models.ForeignKey(Parent, default=None)
	# student = models.OneToOneField(AUTH_USER_MODEL, default=None)
	relation = models.CharField(max_length=10, choices=(
		('Mother', 'Mother'),
		('Father', 'Father'),
		('Guardian', 'Guardian')),
		default='Guardian'
	)

	def __str__(self):
		return "{0}  {1}".format(self.parent, self.relation)
