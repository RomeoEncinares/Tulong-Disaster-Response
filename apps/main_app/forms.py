from django import forms
from .models import *

class RescueeForm(forms.ModelForm):
    class Meta:
        model = Rescuee
        fields = '__all__'

        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'disaster': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control'}),
            'chidlren': forms.TextInput(attrs={'class': 'form-control'}),
            'senior': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),
        }
