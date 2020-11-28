from django import forms
from django.forms import ModelForm
from .models import *

class RescueeForm(forms.ModelForm):

    # Forms with styling
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Name'}))
    disaster = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Type of Disaster'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Location'}))
    total = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : ' Total Number of Rescuees'}))
    children = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Number of Children'}))
    senior = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Number of Senior Citizens'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Any other Important Information'}))
    status_choices = (
        ('Waiting','Waiting for Rescuers'),
        ('Going','Rescuers on the Way'),
        )
    status = forms.ChoiceField(widget=forms.Select, choices=status_choices)

    class Meta:
        model = Rescuee
        fields = '__all__'
