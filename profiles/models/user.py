from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """extended class for User."""

    date_of_birth = models.DateField(null=True, blank=True)
    user_type = models.CharField(max_length=7, choices=(
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Parent', 'Parent'),
    ))

    gender = models.CharField(max_length=6, choices=(
		('', ''),
		('Male', 'Male'),
		('Female', 'Female')),
		default='',
        blank=True
	)

    def __str__(self):
		return "{0} {1}".format(self.username, self.first_name)
