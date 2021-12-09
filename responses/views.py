from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .forms import ResponseForm
from .utilities.custom_url_views import ResponseCollectionView


class ResponseThanksView(TemplateView):
    template_name = 'response/thanks.html'


ResponseCollectionView
