from django.urls import path

from .views import UpdateSeniorityView, SeniorityDeleteView

urlpatterns = [
    path('seniority_update/<int:pk>', UpdateSeniorityView.as_view(),
         name='seniority_update'),
    path('seniority_delete/<int:pk>',
         SeniorityDeleteView.as_view(), name='seniority_delete')
]
