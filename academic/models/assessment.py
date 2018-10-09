# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save

class Assessment(models.Model):
    exam = models.ForeignKey('Exam')
    subject = models.ForeignKey('Subject')
    roll_no = models.IntegerField(editable=False)
    student = models.ForeignKey('profiles.Student')
    course = models.ForeignKey('Course', editable=False)
    department = models.ForeignKey('Department', editable=False)

    attendance = models.CharField(max_length=1, choices=[
        ("A", "Absent"),
        ("P", "Present")
    ], editable=False)

    marks_scored = models.IntegerField()
    out_of = models.IntegerField(editable=False)

    status = models.CharField(max_length=6, choices=[
        ('Failed', "Failed"),
        ('Passed', "Passed"),
    ], editable=False)

    def __str__(self):
        return str(self.id)

def validate(sender, instance=None, **kwargs):
    """
        check attendance if not present then mark the score as zero
        validate marks_scored vs out_of marks,
        auto fetch and save course and department from Subject
    """
    from profiles.models import Student
    from . import Attendance, Exam, Subject
    attendance = Attendance.objects.filter(student=instance.student,
        attendance_date=instance.exam.exam_date)
    attendance = attendance and attendance[0]

    instance.roll_no = instance.student.roll_no
    instance.course = instance.subject.course
    instance.department = instance.subject.department
    instance.attendance = attendance.attendance
    instance.out_of = instance.subject.max_marks
    instance.status = "Failed" \
        if instance.marks_scored < instance.subject.passing_marks else "Passed"

pre_save.connect(validate, sender=Assessment)
