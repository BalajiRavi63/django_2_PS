from django import forms
from django.db.models import fields
from .models import details

class DetailsForm(forms.ModelForm):
    class Meta:
        model = details
        fields = ['name', 'vendor_name', 'specality', 'description', 'address1', 'district', 'phoneno', 'food_pic']

class SearchForm(forms.Form):
    city = forms.CharField(max_length = 20)