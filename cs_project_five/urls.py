
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shiftbid/', include('shiftbid.urls')),
    path('seniority/', include('seniority.urls')),
    path('shift/', include('shift.urls')),
    path('response/', include('responses.urls')),
]
