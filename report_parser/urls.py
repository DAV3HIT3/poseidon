
from django.urls import path

from .views import *

urlpatterns = [
    path('/', UserReportList.as_view(), name='report-list'),
    path('/add', UserReportAdd.as_view(), name='report-add'),
    path('/<int:pk>', UserReportDetail.as_view(), name='report-detail'),
    path('/<int:pk>/edit', UserReportUpdate.as_view(), name='report-update'),
    path('/<int:pk>/delete', UserReportDelete.as_view(), name='report-delete'),
]
