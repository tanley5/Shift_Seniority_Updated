from django import forms
from shift.models import Shift
from shiftbid.models import Shiftbid


class ResponseForm(forms.Form):
    Shiftbid = forms.ModelMultipleChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        self.report_name = kwargs.pop('report_name')
        super(ResponseForm, self).__init__(*args, **kwargs)
        self.fields['Shiftbid'].queryset = Shift.objects.exclude(
            agent_email__contains='@').filter(report=Shiftbid.objects.get(report_name=self.report_name))
        self.fields["agent_email"] = forms.EmailField()
