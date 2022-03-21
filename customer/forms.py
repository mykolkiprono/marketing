from django import forms
from django.contrib.auth.models import User
from . import models

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','second_name','country','state','email']
