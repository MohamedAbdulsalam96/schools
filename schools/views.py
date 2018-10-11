from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
	return render(request, "pages/home.html", {
		'args': {
			'title': 'Home'
		},
		'no_sidebar': True
	})

def about(request):
	return render(request, "pages/about.html", {
		'args': {
			'title': 'About Us'
		},
		'no_sidebar': True
	})

def signup(request):
	if request.method == "POST":
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			form.save()

		return redirect("student-list")
	else:
		form = UserCreationForm()

	return render(request, "pages/signup.html", {
		'form': form,
		'no_sidebar': True
	})

def login_user(request):
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect("student-list")
		else:
			print "form", form
	else:
		form = AuthenticationForm()

	return render(request, "pages/login.html", {
		"form": form,
		'no_sidebar': True
	})

def logout_user(request):
	if request.method == "POST":
		logout(request)
		return redirect("/")

def render_base_form(request, form, id, id_field="id", title="", update_url="",
	new_url=""):
	""" render base form """

	return render(request, "layout/base_form.html", {
		"params": {
			id_field: id
		},
		"id_value": id,
		"form": form,
        "new_url": new_url,
        "update_url": update_url,
		"title": title,
	})
