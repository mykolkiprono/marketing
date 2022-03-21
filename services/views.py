from django.shortcuts import render

# Create your views here.

def services_home(requests):
	return render(requests,'services/services_home.html')
