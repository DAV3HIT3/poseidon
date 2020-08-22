
from django.forms import ModelForm

from .models import *

class UserReportForm(ModelForm):
    class Mets:
        model = UserReport
        fields = ['text', 'json_data']
