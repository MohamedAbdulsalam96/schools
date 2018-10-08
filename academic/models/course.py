# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .department import Department

class Course(models.Model):
    department = models.ForeignKey('Department')
    course_name = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.course_name
