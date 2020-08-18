
from django.forms import ModelForm

from .models import *

class UserReportForm(ModelForm):
    class Meta:
        model = UserReport
        fields = ["text",]
