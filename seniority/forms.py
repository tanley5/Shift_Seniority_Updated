from django import forms
from django.forms import fields
from .models import Seniority


class SeniorityUpdateForm(forms.ModelForm):
    class Meta:
        model = Seniority
        fields = ['agent_net_id', 'agent_email', 'seniority_number']
