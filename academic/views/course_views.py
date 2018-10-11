from academic.models import Course
from django.http import HttpResponse
from schools.views import render_base_form
from django.shortcuts import render, redirect
from profiles.models.user import access_teacher
from academic.forms.course_form import CourseForm
from django.contrib.auth.decorators import login_required

@login_required
def get_course_list(request):
	rows = Course.objects.all()
	return render(request, "layout/base_list.html", {
		'title': 'Course List',
        'list_template': "course/course_list.html",
        'new_url': 'new-course',
		'rows': rows
	})

def save_course(request, course=None):
	# save or create new course
	form = CourseForm(data=request.POST, instance=Course.objects.get(course=course) if course else None)

	if form.is_valid():
		form.save()
		return redirect('course-list')
	else:
		return HttpResponse("Error")

@login_required
@access_teacher()
def delete_course(request, course):
	# delete course from the database
	Course.objects.filter(course=course).delete()
	return redirect('course-list')

# create new course
@login_required
@access_teacher()
def save_update_course(request, course=None):
	if request.method == "POST":
		return save_course(request, course=course)
	else:
		course = Course.objects.get(course=course) if course else None
		form = CourseForm(instance=course)

	return render_base_form(request, form, course, new_url="new-course",
        update_url="update-course")
