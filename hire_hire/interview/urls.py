from django.urls import path

from .views import InterviewFlow, InterviewSettings, Languages

app_name = 'interview'

urlpatterns = [
    path('settings/', InterviewSettings.as_view(), name='settings'),
    path(
        'interview/<int:interview_id>',
        InterviewFlow.as_view(),
        name='interview'
    ),
    path('', Languages.as_view(), name='languages'),
]
