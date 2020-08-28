
from django.urls import path

from .views import *

app_name = "report"
urlpatterns = [
    path('', UserReportList.as_view(), name='list'),
    path('add', UserReportAdd.as_view(), name='add'),
    path('<int:pk>', UserReportDetail.as_view(), name='detail'),
    path('<int:pk>/edit', UserReportUpdate.as_view(), name='update'),
    path('<int:pk>/delete', UserReportDelete.as_view(), name='delete'),
]
