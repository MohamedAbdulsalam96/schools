# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from profiles.models import Student
from django.db.models.signals import pre_save

class Attendance(models.Model):
    student = models.ForeignKey(Student)
    attendance_date = models.DateField()
    attendance = models.CharField(max_length=1, choices=[
        ("A", "Absent"),
        ("P", "Present")
    ])

def validate(sender, instance=None, **kwargs):
    """
        check for the attendance date
    """
    attendance = Attendance.objects.filter(student=instance.student,
        attendance_date=instance.attendance_date)
    if attendance:
        raise Exception("Attendance for {student} is already marked for {date}".format(
            student=instance.student,
            date=instance.attendance_date
        ))

pre_save.connect(validate, sender=Attendance)
