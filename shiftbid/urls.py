from django.urls import path

from .views import ShiftbidListView, ShiftbidDeleteView
from .views import shiftbidCreateView, shiftbidSeniorityShiftListview, shiftbidStart

urlpatterns = [
    path('', ShiftbidListView.as_view(), name='shiftbid_home'),
    path('shiftbid_create', shiftbidCreateView, name='shiftbid_create'),
    path('shiftbid_delete/<int:pk>',
         ShiftbidDeleteView.as_view(), name='shiftbid_delete'),
    path('shiftbid_list/<int:pk>',
         shiftbidSeniorityShiftListview, name='shiftbid_list'),
    path('shiftbid_start/<int:pk>', shiftbidStart, name='shiftbid_start'),
]
