from django.views.generic.base import TemplateView

from django.shortcuts import render

class HomePageview(TemplateView):
    template_name= 'pages/index.html'
