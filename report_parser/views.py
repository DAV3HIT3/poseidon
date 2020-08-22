from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

from atlantis.models import *
from .forms import *

class UserReportList(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = UserReport

class UserReportDetail(LoginRequiredMixin, DetailView):
    model = UserReport

class UserReportAdd(LoginRequiredMixin, CreateView):
    #template_name = 'report_parser/userreport_form.html'
    #form_class = SubmitReportForm

    def form_valid(self, form):
        # Add the logged int user to the form data
        form.instance.user = self.request.user
        # Parse the report data
        #form.parse_report()
        return super().form_valid(form)


class UserReportUpdate(LoginRequiredMixin, UpdateView):
    model = UserReport
    fields = ['text',]

class UserReportDelete(LoginRequiredMixin, DeleteView):
    model = UserReport
    success_url = reverse_lazy('report-list')
