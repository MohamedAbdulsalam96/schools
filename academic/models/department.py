# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.department_name
