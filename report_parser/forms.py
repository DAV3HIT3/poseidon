
from django.forms import ModelForm
from django import forms

from .models import *

class UserReportForm(ModelForm):
    json_data = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = UserReport
        fields = ["text",]
        
