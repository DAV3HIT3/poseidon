from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from account.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

from atlantis.models import *

class UserTurnList(LoginRequiredMixin, ListView):
    model = UserTurn

    def get_queryset(self):
        qs = get_object_or_404(UserTurn, user_faction__user=self.request.user)
        return qs
