from django.urls import path

from interview.views import (
    DuelFinishView,
    DuelFlowAnsweredView,
    DuelFlowQuestionView,
    DuelSettingsView,
    IndexView,
    InterviewFinishView,
    InterviewFlowView,
    InterviewSettingsView,
    LanguagesView,
)

app_name = 'interview'

urlpatterns = [
    path(
        'duel_settings/',
        DuelSettingsView.as_view(),
        name='duel_settings',
    ),
    path(
        'duel/<int:duel_id>/finish/',
        DuelFinishView.as_view(),
        name='duel_finish',
    ),
    path(
        'duel/<int:duel_id>/answer/',
        DuelFlowAnsweredView.as_view(),
        name='duel_answer',
    ),
    path(
        'duel/<int:duel_id>/',
        DuelFlowQuestionView.as_view(),
        name='duel',
    ),
    path(
        'settings/',
        InterviewSettingsView.as_view(),
        name='settings',
    ),
    path(
        'interview/<int:interview_id>/',
        InterviewFlowView.as_view(),
        name='interview',
    ),
    path(
        'interview/finish/',
        InterviewFinishView.as_view(),
        name='finish',
    ),
    path(
        'languages/',
        LanguagesView.as_view(),
        name='languages',
    ),
    path(
        '',
        IndexView.as_view(),
        name='index',
    ),
]
