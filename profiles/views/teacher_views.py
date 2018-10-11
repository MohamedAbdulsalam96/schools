from django.http import HttpResponse
from profiles.models import Teacher
from django.shortcuts import render, redirect
from profiles.models.user import access_teacher
from profiles.forms.teacher_form import TeacherForm
from django.contrib.auth.decorators import login_required

@login_required
@access_teacher()
def get_teacher_list(request):
	rows = Teacher.objects.all()
	return render(request, "layout/base_list.html", {
		'title': 'Teacher List',
        'list_template': "teacher/teacher_list.html",
        'new_url': 'new-teacher',
		'rows': rows
	})

@login_required
@access_teacher()
def get_teacher_profile(request, id):
	teacher = Teacher.objects.get(id=id)
	return render(request, "teacher/teacher_profile.html", {
		'doc': teacher,
	})

def save_teacher(request, id=None):
	# save or create new teacher
	form = TeacherForm(data=request.POST, instance=Teacher.objects.get(id=id) if id else None)
	if form.is_valid():
		form.save()
		return redirect('teacher-list')
	else:
		return HttpResponse("Error")

@login_required
@access_teacher()
def delete_teacher(request, id):
	# delete teacher from the database
	Teacher.objects.filter(id=id).delete()

	return redirect('teacher-list')

# create new teacher
@login_required
@access_teacher()
def save_update_teacher(request, id=None):
	if request.method == "POST":
		return save_teacher(request, id=id)
	else:
		teacher = Teacher.objects.get(id=id) if id else None
		form = TeacherForm(instance=teacher)

	return render(request, "teacher/teacher_form.html", {
		"form": form,
		"title": "Update teacher" if id else "Create New",
		"id": id
	})
