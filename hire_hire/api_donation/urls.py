from django.urls import path

from api_donation.views import DonationView

app_name = 'api_donation'

urlpatterns = [
    path('donation/', DonationView.as_view(), name='donation'),
]
