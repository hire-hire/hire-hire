from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView, View

from .exceptions import CustomException
from .models import Interview, Language, Question


DEFAULT_QUESTIONS_COUNT = 10


class Languages(TemplateView):

    template_name = 'pages/programming.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['languages'] = Language.objects.all()
        return context


class InterviewSettings(TemplateView):

    template_name = 'pages/test-settings.html'

    def post(self, request, *args, **kwargs):
        count = request.POST.get('questions-count')
        if count:
            try:
                count = int(count)
            except CustomException:
                count = DEFAULT_QUESTIONS_COUNT
        else:
            count = DEFAULT_QUESTIONS_COUNT
        questions = Question.objects.random(count)
        settings = dict()
        if request.user.is_authenticated:
            settings['user'] = request.user
        interview = Interview.objects.create(**settings)
        for question in questions:
            interview.questions.add(question)
        return HttpResponseRedirect(
                reverse('interview:interview', kwargs={'interview_id': interview.pk}))


class InterviewFlow(TemplateView):

    template_name = 'pages/challenge.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        interview = get_object_or_404(Interview, pk=kwargs.get('interview_id'))
        context['questions'] = interview.questions.all()
        return context


class InterviewFinish(TemplateView):

    template_name = 'pages/test-finished.html'
