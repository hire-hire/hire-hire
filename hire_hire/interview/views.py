from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from interview.models import (
    Duel,
    DuelPlayer,
    DuelQuestion,
    Interview,
    Language,
    Question,
)
from interview.services import get_question_count, create_duel


class LanguagesView(ListView):
    model = Language
    template_name = 'interview/interviews.html'


class IndexView(TemplateView):
    template_name = 'interview/index.html'


class InterviewSettingsView(TemplateView):
    template_name = 'interview/test-settings.html'

    def post(self, request, *args, **kwargs):
        count = get_question_count(request.POST, 'questions-count')

        options = dict()
        if request.user.is_authenticated:
            options['user'] = request.user

        interview = Interview.objects.create(**options)
        interview.questions.add(
            *Question.objects.get_random_questions(count),
        )

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


class DuelSettingsView(TemplateView):
    template_name = 'interview/duel-settings.html'

    def post(self, request, *args, **kwargs):
        duel = create_duel(request)

        return HttpResponseRedirect(
            reverse(
                'interview:duel',
                kwargs={'duel_id': duel.pk},
            )
        )


class DuelFlowQuestionView(TemplateView):
    template_name = 'interview/duel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        duel = get_object_or_404(
            Duel.objects.select_related(),
            pk=kwargs.get('duel_id')
        )
        context['duel_id'] = duel.pk
        context['can_choose_winner'] = False

        context['player1'], context['player2'] = duel.players.all()
        context['duel_question'] = duel.questions.filter(is_answered=False).first()  # нельзя model manager заюзать :(

        return context

    def _finish_duel(self, context):
        if not context.get('duel_question'):
            return HttpResponseRedirect(
                reverse(
                    'interview:duel_finish',
                    kwargs={'duel_id': context.get('duel_id')},
                )
            )
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self._finish_duel(context)


class DuelFlowAnsweredView(DuelFlowQuestionView):
    template_name = 'interview/duel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_choose_winner'] = True
        duel_question = context.get('duel_question')
        if duel_question:
            duel_question.is_answered = True
            duel_question.save()
        return context

    def post(self, request, *args, **kwargs):
        duel = get_object_or_404(
            Duel.objects.select_related(),
            pk=kwargs.get('duel_id')
        )
        winner_id = int(request.POST.get('duel-radio-player'))
        if duel.players.filter(pk=winner_id).exists():
            winner = duel.players.filter(pk=winner_id).first()
            winner.good_answers_count += 1
            winner.save()
        else:
            duel.wrong_answers_count += 1
            duel.save()
        return HttpResponseRedirect(
            reverse(
                'interview:duel',
                kwargs={'duel_id': duel.pk}
            )
        )


class DuelFinishView(TemplateView):
    template_name = 'interview/duel-results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        duel = get_object_or_404(
            Duel.objects.select_related(),
            pk=kwargs.get('duel_id')
        )
        context['duel'] = duel
        context['player1'] = duel.players.first()
        context['player2'] = duel.players.last()
        return context
