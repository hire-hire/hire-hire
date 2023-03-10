from django.urls import path

from .views import AddQuestionFinishView, AddQuestionView

app_name = 'addquestion'

urlpatterns = [
    path('', AddQuestionView.as_view(), name='addquestion', ),
    path('finished/',
         AddQuestionFinishView.as_view(), name='finished', ),
]
