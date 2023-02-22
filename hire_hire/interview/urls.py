from django.urls import path

from .views import (
    Index,
    InterviewFinish,
    InterviewFlow,
    InterviewSettings,
    Languages,
)


app_name = 'interview'

urlpatterns = [
    path('settings/', InterviewSettings.as_view(), name='settings'),
    path(
        'interview/<int:interview_id>',
        InterviewFlow.as_view(),
        name='interview'
    ),
    path('interview/finish/', InterviewFinish.as_view(), name='finish'),
    path('languages/', Languages.as_view(), name='languages'),
    path('', Index.as_view(), name='index'),
]
