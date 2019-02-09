from django import forms
from .models import *

#create your forms here

class ItemCreationForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['title', 'price', 'category', 'description']