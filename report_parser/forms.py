
from django.forms import ModelForm
from django import forms

from .models import *

class UserReportForm(ModelForm):
    class Meta:
        model = UserReport
        fields = ["text",]
        
