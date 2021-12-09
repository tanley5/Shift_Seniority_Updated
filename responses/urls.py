from django.urls import path

from .views import ResponseThanksView, ResponseCollectionView
#from .utilities.custom_url_views import urlpatterns as custom_url_patterns

urlpatterns = [
    path('response_thanks', ResponseThanksView.as_view(), name='response_thanks'),
    path('response_collection/<report_name>',
         ResponseCollectionView.as_view(), name='shiftbid_response'),
]
