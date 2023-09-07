from django.urls import path

from api.views import CustomerListAPIView, DealCreateAPIView

app_name = 'api'

urlpatterns = [
    path('v1/deals/', DealCreateAPIView.as_view(), name='deals-create'),
    path('v1/customers/', CustomerListAPIView.as_view(), name='customers-list'),
]
