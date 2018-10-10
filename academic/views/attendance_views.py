from django.http import HttpResponse
from django.shortcuts import render, redirect
from academic.models import Attendance
from academic.forms.attendance_form import AttendanceForm
from schools.views import render_base_form

def get_attendance_list(request):
	rows = Attendance.objects.all()
	return render(request, "layout/base_list.html", {
		'title': 'Attendance List',
        'list_template': "attendance/attendance_list.html",
        'new_url': 'new-attendance',
		'rows': rows
	})

def save_attendance(request, id=None):
	# save or create new attendance
	form = AttendanceForm(data=request.POST, instance=Attendance.objects.get(id=id) if id else None)

	if form.is_valid():
		form.save()
		return redirect('attendance-list')
	else:
		return HttpResponse("Error")

def delete_attendance(request, id):
	# delete attendance from the database
	Attendance.objects.filter(id=id).delete()
	return redirect('attendance-list')

# create new attendance
def save_update_attendance(request, id=None):
	if request.method == "POST":
		return save_attendance(request, id=id)
	else:
		attendance = Attendance.objects.get(id=id) if id else None
		form = AttendanceForm(instance=attendance)

	return render_base_form(request, form, id, new_url="new-attendance",
        update_url="update-attendance")
