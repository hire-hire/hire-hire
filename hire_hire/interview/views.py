from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic import ListView, TemplateView
from django.conf import settings

from .exceptions import CustomException
from .models import Interview, Language, Question


class Languages(ListView):
    model = Language
    template_name = 'pages/interviews.html'


class Index(TemplateView):
    template_name = 'pages/index.html'


class InterviewSettings(TemplateView):
    template_name = 'pages/test-settings.html'

    def post(self, request, *args, **kwargs):
        count = request.POST.get(
            'questions-count', default=settings.DEFAULT_QUESTIONS_COUNT
        )

        try:
            count = int(count)
        except CustomException:
            count = settings.DEFAULT_QUESTIONS_COUNT

        questions = Question.objects.random(count)
        options = dict()
        if request.user.is_authenticated:
            options['user'] = request.user

        interview = Interview.objects.create(**options)
        interview.questions.add(*questions)

        return HttpResponseRedirect(
            reverse(
                'interview:interview',
                kwargs={'interview_id': interview.pk}
            )
        )


class InterviewFlow(TemplateView):
    template_name = 'pages/challenge.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        interview = get_object_or_404(Interview, pk=kwargs.get('interview_id'))
        context['questions'] = interview.questions.all()
        return context


class InterviewFinish(TemplateView):
    template_name = 'pages/test-finished.html'
