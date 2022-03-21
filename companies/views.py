from django.shortcuts import render

# Create your views here.

def company_home(requests):
	return render(requests,'company/company_home.html')

