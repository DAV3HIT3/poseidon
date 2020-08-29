from django.db import models
from django.conf import settings
from django.urls import reverse

#from atlantis.models import *

# Atlantis user turn report
class UserReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    json_data = models.JSONField(default=dict)

    def get_absolute_url(self):
        return reverse('report:detail', kwargs={'pk':self.pk})
