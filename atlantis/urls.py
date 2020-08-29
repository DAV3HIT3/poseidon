
from django.urls import path

from .views import *

app_name = 'atlantis'
urlpatterns = [
    path('turns/', UserTurnList.as_view(), name='turn-list'),
    path('turns/<int:pk>', UserTurnDetail.as_view(), name='turn-detail'),

    path('units/', UnitList.as_view(), name='unit-list'),
    path('units/<int:pk>', UnitDetail.as_view(), name='unit-detail'),

    #path('units/<int:pk>/turns/', UnitTurnList.as_view(), name='unit-turn-list'),
    #path('units/<int:pk>/turns/<int:pk>', UnitTurnDetail.as_view(), name='unit-turn-detail'),
]
