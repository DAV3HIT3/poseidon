
from django.urls import path

from .views import *

app_name = 'hexmap'
urlpatterns = [
        path('regions/', region_list_json, name='region-list'),
        path('regions/<int:pk>', region_detail_json, name='region-detail'),
]
