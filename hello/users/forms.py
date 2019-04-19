from django import forms
from .models import Product


class Contact(forms.Form):
    name = forms.CharField(label = 'your name :',max_length = 100)
    email = forms.EmailField()
    message = forms.CharField(widget= forms.Textarea)
    


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [

		'product_name', 
		'product_id'



		]

