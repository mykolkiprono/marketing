"""marketing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from companies.views import company_home
from customer.views import customer_home
from services.views import services_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company_home/',company_home,name='company_home'),
    path('customer_home/',customer_home,name='customer_home'),
    path('services_home/',services_home,name='services_home'),
]
