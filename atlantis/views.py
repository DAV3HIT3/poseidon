from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy

from account.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

from atlantis.models import *

# -------------------------------------------------------------------------------------------
# User reports turn list
# -------------------------------------------------------------------------------------------
class UserTurnList(LoginRequiredMixin, ListView):
    model = UserTurn
    paginate_by = 10

    def get_queryset(self):
        qs = UserTurn.objects.filter(user_faction__user=self.request.user)
        return qs

# -------------------------------------------------------------------------------------------
# User report turn detail
# -------------------------------------------------------------------------------------------
class UserTurnDetail(LoginRequiredMixin, DetailView):
    model = UserTurn



# -------------------------------------------------------------------------------------------
# Unit list
# -------------------------------------------------------------------------------------------
class UnitList(LoginRequiredMixin, ListView):
    model = Unit
    paginate_by = 10

# -------------------------------------------------------------------------------------------
# Unit detail
# -------------------------------------------------------------------------------------------
class UnitDetail(LoginRequiredMixin, DetailView):
    model = Unit


# -------------------------------------------------------------------------------------------
# Unit turn list (Detail unit view, list all associated turns)
# -------------------------------------------------------------------------------------------
class UnitTurnList(LoginRequiredMixin, DetailView):
    model = UnitDetail

    def get_queryset(self):
        qs = UnitDetail.objects.filter(turn__user_faction__user=self.request.user)
        return qs

# -------------------------------------------------------------------------------------------
#
# -------------------------------------------------------------------------------------------
class UnitTurnDetail(LoginRequiredMixin, DetailView):
    model = UnitDetail


# -------------------------------------------------------------------------------------------
# Main map view
# -------------------------------------------------------------------------------------------
class MapView(LoginRequiredMixin, TemplateView):
    template_name = 'atlantis/map.html'



