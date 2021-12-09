from django.views.generic.edit import UpdateView, DeleteView

from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Shift
from .forms import ShiftUpdateForm

# Create your views here.


class ShiftUpdateView(UpdateView):
    model = Shift
    template_name = 'shift/shift_update.html'
    form_class = ShiftUpdateForm
    success_url = reverse_lazy('shiftbid_home')


class ShiftDeleteView(DeleteView):
    model = Shift
    template_name = 'shift/shift_delete.html'
    success_url = reverse_lazy('shiftbid_home')
