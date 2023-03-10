from django.urls import path

from add_question.views import AddQuestionFinishView, AddQuestionView

app_name = 'add_question'

urlpatterns = [
    path(
        '',
        AddQuestionView.as_view(),
        name='add_question'),
    path(
        'finished/',
        AddQuestionFinishView.as_view(),
        name='finished'),
]
