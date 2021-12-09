from django.views.generic.edit import UpdateView, DeleteView

from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Seniority
from .forms import SeniorityUpdateForm

# Create your views here.


class UpdateSeniorityView(UpdateView):
    model = Seniority
    template_name = 'seniority/seniority_update.html'
    form_class = SeniorityUpdateForm
    success_url = reverse_lazy('shiftbid_home')


class SeniorityDeleteView(DeleteView):
    model = Seniority
    template_name = 'seniority/seniority_delete.html'
    success_url = reverse_lazy('shiftbid_home')
