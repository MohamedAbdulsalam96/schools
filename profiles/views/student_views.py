from django.http import HttpResponse
from schools.views import render_base_form
from profiles.models.student import Student
from django.shortcuts import render, redirect
from profiles.models.user import access_teacher
from profiles.forms.student_form import StudentForm
from django.contrib.auth.decorators import login_required

@login_required
def get_student_list(request):
    students = Student.objects.all()
    return render(request, "layout/base_list.html", {
		'title': 'Student List',
        'list_template': "student/student_list.html",
        'new_url': 'new-student',
		'rows': students
	})

@login_required
def get_student_profile(request, prn):
	student = Student.objects.get(prn=prn)
	return render(request, "student/student_profile.html", {
		'doc': student,
		'parents': student.parents.all()
	})

def save_student(request, prn=None):
	# save or create new student
	form = StudentForm(data=request.POST, instance=Student.objects.get(prn=prn) \
        if prn else None)

	if form.is_valid():
		form.save()
		return redirect('student-list')
	else:
		return HttpResponse("Error")

@login_required
@access_teacher()
def delete_student(request, prn):
	# delete student from the database
	Student.objects.filter(prn=prn).delete()

	return redirect('student-list')

# create new student
@login_required
@access_teacher()
def save_update_student(request, prn=None):
	if request.method == "POST":
		return save_student(request, prn=prn)
	else:
		student = Student.objects.get(prn=prn) if prn else None
		form = StudentForm(instance=student)

	return render_base_form(request, form, prn, id_field="prn", new_url="new-student",
        update_url="update-student")
