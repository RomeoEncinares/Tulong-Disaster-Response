from django import forms
from .models import *

class RescueeForm(forms.ModelForm):

    # Forms with styling
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Name'}))
    disaster = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Type of Disaster'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Location'}))
    total = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : ' Total Number of Rescuees'}))
    children = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Number of Children'}))
    senior = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Number of Senior Citizens'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Any other Important Information'}))

    class Meta:
        model = Rescuee
        fields = '__all__'
