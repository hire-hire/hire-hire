from django.urls import path

from duel.views import (
    DuelFinishView,
    DuelFlowAnsweredView,
    DuelFlowQuestionView,
    DuelSettingsView,
)

app_name = 'duel'

urlpatterns = [
    path(
        'settings/',
        DuelSettingsView.as_view(),
        name='duel_settings',
    ),
    path(
        '<int:duel_id>/finish/',
        DuelFinishView.as_view(),
        name='duel_finish',
    ),
    path(
        '<int:duel_id>/answer/',
        DuelFlowAnsweredView.as_view(),
        name='duel_answer',
    ),
    path(
        '<int:duel_id>/',
        DuelFlowQuestionView.as_view(),
        name='duel',
    ),
]
