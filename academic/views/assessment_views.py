from django.http import HttpResponse
from django.shortcuts import render, redirect
from academic.models import Assessment
from academic.forms.assessment_form import AssessmentForm
from schools.views import render_base_form

def get_assessment_list(request):
	assessment = Assessment.objects.all()
	return render(request, "assessment/assessment_list.html", {
		'title': 'Assessment List',
		'rows': assessment
	})

def save_assessment(request, id=None):
	# save or create new assessment
	form = AssessmentForm(data=request.POST, instance=Assessment.objects.get(id=id) if id else None)

	if form.is_valid():
		form.save()
		return redirect('assessment-list')
	else:
		return HttpResponse("Error")

def delete_assessment(request, id):
	# delete assessment from the database
	Assessment.objects.filter(id=id).delete()
	return redirect('assessment-list')

# create new assessment
def save_update_assessment(request, id=None):
	if request.method == "POST":
		return save_assessment(request, id=id)
	else:
		assessment = Assessment.objects.get(id=id) if id else None
		form = AssessmentForm(instance=assessment)

	return render_base_form(request, form, id, new_url="new-assessment",
        update_url="update-assessment")
