from django import forms
from FIRSTAPPLICATION.models import *

class CustomerForm(forms.Form):
    name = forms.CharField()

