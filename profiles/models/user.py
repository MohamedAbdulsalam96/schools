from django.db import models
from functools import wraps
from django.http import HttpResponse
from django.shortcuts import render, redirect
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

def access_teacher():
    def decorator(func):
        def inner_decorator(request, *args, **kwargs):
            if request.user:
                user_details = User.objects.filter(username=request.user)
                user_details = user_details and user_details[0]
                if not user_details or user_details.user_type in ["Student", "Parent"]:
                    return redirect('student-list')

                return func(request, *args, **kwargs)
            else:
                return redirect('login')
        return wraps(func)(inner_decorator)
    return decorator
