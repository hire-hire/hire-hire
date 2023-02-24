from django.urls import path

from contributors.views import ContributorsView

app_name = 'contributors'

urlpatterns = [
    path('', ContributorsView.as_view(), name='contributors_list'),
]
