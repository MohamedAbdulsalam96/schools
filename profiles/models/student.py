# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.utils.dateformat import format

import datetime
from .user import User
from .parent import ParentItem

class Student(models.Model):
	# Personal Information
	user = models.OneToOneField(User, default=None, related_name="user")
	title = models.CharField(max_length=100, editable=False)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	parents = models.ManyToManyField(ParentItem)

	# Academic Information
	date_of_joining = models.DateField()
	prn = models.CharField(max_length=50,
		editable=False)
	roll_no = models.IntegerField()
	standard = models.ForeignKey('Standard')
	division = models.ForeignKey('Division')
	# previous years details

	# Timestamps
	creation = models.DateTimeField(auto_now_add=True, editable=False)
	modified = models.DateTimeField(auto_now=True, editable=False)
	created_by = models.ForeignKey(User, default=None)

	def __str__(self):
		return " ".join([self.prn, self.title, str(self.standard), str(self.division),
			str(self.roll_no)])

def validate(sender, instance=None, **kwargs):
	"""
		set the values to fields and validate the Student information raise the
		error if any
		# set prn, title for the student before save
	"""

	max_id = 1

	try:
		max_id = Student.objects.latest("id").id + 1
	except Exception as e:
		pass

	instance.title = " ".join([instance.first_name, instance.last_name])
	instance.prn = "{date}{max_id}".format(
		date=format(datetime.datetime.today(), "Ymd"),
		max_id="%04d"%(max_id or 1))
	# ToDo get the current logged in user

pre_save.connect(validate, sender=Student)
