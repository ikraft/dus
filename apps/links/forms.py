from django import forms
from .models import Link

class Link(forms.Form):
    link = forms.Urlfield()
    
