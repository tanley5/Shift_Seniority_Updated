from django.urls import path

from .views import ShiftUpdateView, ShiftDeleteView

urlpatterns = [
    path('shift_update/<int:pk>', ShiftUpdateView.as_view(), name='shift_update'),
    path('shift_delete/<int:pk>', ShiftDeleteView.as_view(), name='shift_delete'),
]
