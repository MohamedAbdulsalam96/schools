# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date
from academic.models import Subject

class Exam(models.Model):
    exam = models.CharField(primary_key=True, max_length=50)
    exam_date = models.DateField(default=date.today)

    def __str__(self):
        return self.exam
