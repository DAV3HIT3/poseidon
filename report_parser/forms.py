
from django.forms import ModelForm
from django import forms

from .models import *

class UserReportForm(ModelForm):
    json_data = forms.CharField()
    class Meta:
        model = UserReport
        fields = ["text", "json_data"]
        
