from django.urls import path

from api.views import DealCreateAPIView

app_name = 'api'

urlpatterns = [
    path('v1/deals/', DealCreateAPIView.as_view(), name='deals-create'),
]
