from django import forms

from .models import Shift


class ShiftUpdateForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['shift', 'agent_email']
