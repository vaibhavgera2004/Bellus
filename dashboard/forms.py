from django import forms
from django.forms import ModelForm
from core.models import Service, Customer
from django.contrib.auth.models import User

class AddServiceForm(ModelForm):
	class Meta:
		model = Service
		fields = ('name','price','image')

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'price': forms.NumberInput(attrs={'class': 'form-control'}),
			'image': forms.FileInput(attrs={'class': 'form-control'})
		}


# class AdminForm(ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ('username', 'password')
	
		