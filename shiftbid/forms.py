from django import forms

from .utils.handle_shiftbid_forms import handle_shiftbid_creation, handle_shift_creation, handle_seniority_creation


class ShiftbidCreateForm(forms.Form):
    report_name = forms.CharField(label="Shiftbid Report Name", max_length=250)
    shift_file = forms.FileField()
    seniority_file = forms.FileField()

    def handle_cleaned_shiftbid(self):
        report_name = self.cleaned_data['report_name']
        shiftfile = self.cleaned_data["shift_file"]
        seniorityfile = self.cleaned_data["seniority_file"]

        handle_shiftbid_creation(report_name)
        handle_shift_creation(shiftfile, report_name)
        handle_seniority_creation(seniorityfile, report_name)
