from django.http import HttpResponse
from django.shortcuts import render

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
