from django.urls import path
from . import views


app_name = 'test_interview'

urlpatterns = [
    path('questions/', views.InterviewView.as_view(), name='interview'),
]
