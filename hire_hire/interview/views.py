from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, FormView, TemplateView

from interview.forms import InterviewSettingsForm
from interview.models import Interview, Language
from interview.services import create_interview


class LanguagesView(ListView):
    model = Language
    template_name = 'interview/interviews.html'


class InterviewSettingsView(LoginRequiredMixin, FormView):
    form_class = InterviewSettingsForm
    template_name = 'interview/test-settings.html'

    def form_valid(self, form):
        interview = create_interview(
            user=self.request.user,
            count=form.cleaned_data['questions_count'],
        )

        self.success_url = reverse(
            'interview:interview',
            kwargs={'interview_id': interview.pk},
        )
        return super().form_valid(form)


class InterviewFlowView(LoginRequiredMixin, TemplateView):
    template_name = 'interview/challenge.html'

    def get_context_data(self, interview_id, **kwargs):
        context = super().get_context_data(**kwargs)
        interview = get_object_or_404(
            Interview.objects.get_interview_by_user(
                interview_pk=interview_id,
                user=self.request.user,
            )
        )
        context['questions'] = interview.questions.all()
        return context


class InterviewFinishView(TemplateView):
    template_name = 'interview/test-finished.html'
