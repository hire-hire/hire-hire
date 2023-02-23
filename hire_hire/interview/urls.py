from django.urls import path

from interview.views import (
    InterviewFinishView,
    InterviewFlowView,
    InterviewSettingsView,
    LanguagesView,
)

app_name = 'interview'

urlpatterns = [
    path(
        'settings/',
        InterviewSettingsView.as_view(),
        name='settings',
    ),
    path(
        '<int:interview_id>/',
        InterviewFlowView.as_view(),
        name='interview',
    ),
    path(
        'finish/',
        InterviewFinishView.as_view(),
        name='finish',
    ),
    path(
        'languages/',
        LanguagesView.as_view(),
        name='languages',
    ),
]
