from django.urls import path

from .views import AddQuestionView

app_name = 'addquestion'

urlpatterns = [
    path('', AddQuestionView.as_view(), name='addquestion', ),
]
