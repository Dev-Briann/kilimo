from django import forms 
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Contact