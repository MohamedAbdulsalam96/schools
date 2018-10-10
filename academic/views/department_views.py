from django.http import HttpResponse
from django.shortcuts import render, redirect
from academic.models import Department
from academic.forms.department_form import DepartmentForm
from schools.views import render_base_form

def get_department_list(request):
	rows = Department.objects.all()
	return render(request, "layout/base_list.html", {
		'title': 'Department List',
        'list_template': "department/department_list.html",
        'new_url': 'new-department',
		'rows': rows
	})

def save_department(request, department=None):
	# save or create new department
	form = DepartmentForm(data=request.POST,
        instance=Department.objects.get(department=department) if department else None)

	if form.is_valid():
		form.save()
		return redirect('department-list')
	else:
		return HttpResponse("Error")

def delete_department(request, department):
	# delete department from the database
	Department.objects.filter(department=department).delete()
	return redirect('department-list')

# create new department
def save_update_department(request, department=None):
	if request.method == "POST":
		return save_department(request, department=department)
	else:
		department = Department.objects.get(department=department) if department else None
		form = DepartmentForm(instance=department)

	return render_base_form(request, form, department, id_field="department",
        new_url="new-department", update_url="update-department")
