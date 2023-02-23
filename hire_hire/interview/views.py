from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from interview.models import (
    Interview,
    Language,
)
from interview.services import create_interview


class LanguagesView(ListView):
    model = Language
    template_name = 'interview/interviews.html'


class InterviewSettingsView(TemplateView):
    template_name = 'interview/test-settings.html'

    def post(self, request, *args, **kwargs):
        interview = create_interview(request)

        return HttpResponseRedirect(
            reverse(
                'interview:interview',
                kwargs={'interview_id': interview.pk},
            )
        )


class InterviewFlowView(TemplateView):
    template_name = 'interview/challenge.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        interview = get_object_or_404(Interview, pk=kwargs.get('interview_id'))
        context['questions'] = interview.questions.all()
        return context


class InterviewFinishView(TemplateView):
    template_name = 'interview/test-finished.html'
