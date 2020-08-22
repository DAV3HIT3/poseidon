
from django.forms import ModelForm
from django import forms

from .models import *

class SubmitReportForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    json_data = forms.CharField(widget=forms.Textarea)

    def parse_report(self):
        # get the parsed json data and create the appropriate models
        pass
