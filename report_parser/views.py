from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.forms import Textarea
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

from account.mixins import LoginRequiredMixin
#from django.contrib.auth.mixins import LoginRequiredMixin

from prettyjson import PrettyJSONWidget

from atlantis.models import *
from .forms import *
from .parse_report import *

class UserReportList(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = UserReport

    def get_queryset(self):
        qs = UserReport.objects.filter(user=self.request.user)
        return qs

class UserReportDetail(LoginRequiredMixin, DetailView):
    model = UserReport

    def get_queryset(self):
        # Filter by loggin user
        qs = super(UserReporDetail,self).get_queryset().filter(user=self.request.user)

class UserReportAdd(LoginRequiredMixin, CreateView):
    model = UserReport
    fields = ['text', 'json_data']

    def form_valid(self, form):
        # Add the logged int user to the form data
        form.instance.user = self.request.user

        # Create report parser, init with JSON format report to report parser
        report_parser = ParseAtlantisReport(form.instance.json_data)
        # Call parser method, pass in current user
        report_valid = report_parser.parseJson(self.request.user)

        return super().form_valid(form)


class UserReportUpdate(LoginRequiredMixin, UpdateView):
    model = UserReport
    fields = ['text',]

class UserReportDelete(LoginRequiredMixin, DeleteView):
    model = UserReport
    success_url = reverse_lazy('report:list')
