from django.urls import path

from .views import (
    DuelFinish,
    DuelFlowAnswered,
    DuelFlowQuestion,
    DuelSettings,
    Index,
    InterviewFinish,
    InterviewFlow,
    InterviewSettings,
    Languages,
)


app_name = 'interview'

urlpatterns = [
    path(
        'duel_settings/',
        DuelSettings.as_view(),
        name='duel_settings',),
    path(
        'duel/<int:duel_id>/finish/',
        DuelFinish.as_view(),
        name='duel_finish',
    ),
    path(
        'duel/<int:duel_id>/answer/',
        DuelFlowAnswered.as_view(),
        name='duel_answer',
    ),
    path(
        'duel/<int:duel_id>',
        DuelFlowQuestion.as_view(),
        name='duel',
    ),
    path(
        'settings/',
        InterviewSettings.as_view(),
        name='settings',
    ),
    path(
        'interview/<int:interview_id>',
        InterviewFlow.as_view(),
        name='interview',
    ),
    path(
        'interview/finish/',
        InterviewFinish.as_view(),
        name='finish',
    ),
    path(
        'languages/',
        Languages.as_view(),
        name='languages',
    ),
    path('', Index.as_view(), name='index',),
]
