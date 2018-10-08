# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Subject(models.Model):
    course = models.ForeignKey('Course')
    subject = models.CharField(primary_key=True, max_length=50)
    department = models.ForeignKey('Department', editable=False)

    def __str__(self):
        return self.subject
