from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.forms import Textarea
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from prettyjson import PrettyJSONWidget

from atlantis.models import *
from .forms import *
from .parse_report import *

class UserReportList(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = UserReport

class UserReportDetail(LoginRequiredMixin, DetailView):
    model = UserReport

class UserReportAdd(LoginRequiredMixin, CreateView):
    model = UserReport
    fields = ['text', 'json_data']

    def form_valid(self, form):
        # Add the logged int user to the form data
        form.instance.user = self.request.user

        report_parser = ParseAtlantisReport(form.instance.json_data)
        report_parser.parseJson(self.request.user)

        #try:
        #    report_parser = ParseAtlantisReport(form.instance.json_data)
        #    report_parser.parseJson(self.request.user)
        #except Exception as err:
        #    print("Exception occured while parsing report!", err)

        # Continue and save the form
        return super().form_valid(form)



class UserReportUpdate(LoginRequiredMixin, UpdateView):
    model = UserReport
    fields = ['text',]

class UserReportDelete(LoginRequiredMixin, DeleteView):
    model = UserReport
    success_url = reverse_lazy('report-list')
