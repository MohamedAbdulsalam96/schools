from django.http import HttpResponse
from django.shortcuts import render, redirect
from profiles.models.student import Student
from profiles.forms.student_form import StudentForm

def get_student_list(request):
    students = Student.objects.all()
    return render(request, "student/student_list.html", {
		'title': 'Student List',
		'rows': students
	})

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

def delete_student(request, prn):
	# delete student from the database
	Student.objects.filter(prn=prn).delete()

	return redirect('student-list')

# create new student
def save_update_student(request, prn=None):
	if request.method == "POST":
		return save_student(request, prn=prn)
	else:
		student = Student.objects.get(prn=prn) if prn else None
		form = StudentForm(instance=student)

	return render(request, "student/student_form.html", {
		"form": form,
		"title": "Update Student" if prn else "Create New",
		"prn": prn
	})
