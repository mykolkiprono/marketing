from django.shortcuts import render
from .models import Customer

# Create your views here.

def customer_home(requests):
	customer = Customer.objects.all()
	return render(requests,'customer/customer_home.html')
