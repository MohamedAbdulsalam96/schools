from django.http import HttpResponse
from django.shortcuts import render, redirect
from academic.models import Exam
from academic.forms.exam_form import ExamForm
from schools.views import render_base_form

def get_exam_list(request):
	rows = Exam.objects.all()
	return render(request, "layout/base_list.html", {
		'title': 'Exam List',
        'list_template': "exam/exam_list.html",
        'new_url': 'new-exam',
		'rows': rows
	})

def save_exam(request, exam=None):
	# save or create new exam
	form = ExamForm(data=request.POST, instance=Exam.objects.get(exam=exam) if exam else None)

	if form.is_valid():
		form.save()
		return redirect('exam-list')
	else:
		return HttpResponse("Error")

def delete_exam(request, exam):
	# delete exam from the database
	Exam.objects.filter(exam=exam).delete()
	return redirect('exam-list')

# create new exam
def save_update_exam(request, exam=None):
	if request.method == "POST":
		return save_exam(request, exam=exam)
	else:
		exam = Exam.objects.get(exam=exam) if exam else None
		form = ExamForm(instance=exam)

	return render_base_form(request, form, exam, id_field="exam", new_url="new-exam",
        update_url="update-exam")
