from django.db.models import query
from django.urls import path
from django.views.generic.base import View
from django.shortcuts import render

from shiftbid.models import Shiftbid
from responses.forms import ResponseForm
from shift.models import Shift

urlpatterns = []

class ResponseCollectionView(View):
    template_name = 'response/response_collection.html'

    def get(self, request, *args, **kwargs):
        report_name = self.kwargs["report_name"]
        form = ResponseForm(report_name=report_name)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        report_name = self.kwargs["report_name"]
        print(report_name)
        form = ResponseForm(data=request.POST,
                            report_name=report_name)
        context = {'form': form}
        if form.is_valid():
            shift_chosen = form.cleaned_data["Shiftbid"][0].pk
            email = form.cleaned_data["agent_email"]
            handle_response_submission(shift_chosen, email)
            form = ResponseForm(report_name=report_name)
            return render(request, 'response/thanks.html', context)
        return render(request, 'response/response_collection.html', context)


def handle_response_submission(shift_chosen, email):
    shift = Shift.objects.get(pk=shift_chosen)
    shift.agent_email = email
    shift.save()

def get_report_names(pk):
    shiftbid_objects = Shiftbid.objects.get(pk=pk)
    return shiftbid_objects.report_name

def create_url(report_name):
    urlpatterns.append(path(
        f"response_collection/{report_name}", ResponseCollectionView.as_view(), name=f"{report_name}-reponse_path"))


def create_custom_views_url(pk):
    report_name = get_report_names(pk)
    create_url(report_name)

#___________________________________________________
# The method below is for multiple views creation
# def get_report_names():
#     shiftbid_objects = Shiftbid.objects.all()

#     for shiftbid in shiftbid_objects:
#         report_name_list.append(shiftbid.report_name)

# def create_custom_views_url():
#     get_report_names()

#     for report_name in report_name_list:
#         create_url(report_name)

# def spawn_child_elements(report_name):
#     create_url(report_name)
