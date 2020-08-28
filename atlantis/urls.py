
from django.urls import path

from .views import *

app_name = 'atlantis'
urlpatterns = [
    path('', UserTurnList.as_view(), name='turn-list'),
    #path('<int:pk>', TurnDetail.as_view(), name='turn-detail'),
]
