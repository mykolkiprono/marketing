from djabngo import forms
from .models import company

class companyform(forms.ModelForm):
	class Meta:
		model = company
		fiels = ['name','c_image_1','c_image_2','c_image_3','country','state','street']