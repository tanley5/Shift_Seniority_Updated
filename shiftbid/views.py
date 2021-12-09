from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView

from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
import threading

from .models import Shiftbid
from .forms import ShiftbidCreateForm

from shift.models import Shift
from seniority.models import Seniority

from responses.utilities.custom_url_views import create_custom_views_url
from .utils.handle_shiftbid_start import handleShiftbidStart


class ShiftbidListView(ListView):
    model = Shiftbid
    template_name = 'shiftbid/shiftbid_index.html'


class ShiftbidDeleteView(DeleteView):
    model = Shiftbid
    template_name = 'shiftbid/shiftbid_delete.html'
    success_url = reverse_lazy('shiftbid_home')


def shiftbidCreateView(request):
    if request.method == 'POST':
        form = ShiftbidCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.handle_cleaned_shiftbid()
            return HttpResponseRedirect(reverse_lazy('shiftbid_home'))
    else:
        form = ShiftbidCreateForm()

    return render(request, 'shiftbid/shiftbid_create.html', {'form': form})


def shiftbidSeniorityShiftListview(request, pk):
    shiftbid = Shiftbid.objects.get(pk=pk)
    shift_query = Shift.objects.filter(report=shiftbid)
    seniority_query = Seniority.objects.filter(report=shiftbid)
    return render(request, 'shiftbid/shiftbid_list_all.html', {'shift_object': shift_query, 'seniority_object': seniority_query})


def shiftbidStart(request, pk):
    
    if request.method == 'POST':
        create_custom_views_url(pk)
        job_thread = threading.Thread(target=handleShiftbidStart,args=(pk,))
        job_thread.start()
        return render(request, 'shiftbid/shiftbid_start.html')
