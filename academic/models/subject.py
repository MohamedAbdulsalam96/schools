# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError

class Subject(models.Model):
    course = models.ForeignKey('Course')
    subject = models.CharField(primary_key=True, max_length=50)
    department = models.ForeignKey('Department', editable=False)

    # min and max marks
    passing_marks = models.IntegerField(default=35)
    max_marks = models.IntegerField(default=100)

    def __str__(self):
        return self.subject

def validate(sender, instance=None, **kwargs):
    # auto set department from course
    from . import Course

    if instance.passing_marks < 0 or instance.max_marks < 0:
        raise ValidationError("Please enter the valid marks")

    course = Course.objects.filter(course=instance.course)
    instance.department = course and course[0] and course[0].department

pre_save.connect(validate, sender=Subject)
