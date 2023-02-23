from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from interview.models import (
    Duel,
    Interview,
    Language,
)
from interview.services import (
    create_duel,
    set_duel_question_is_answered,
    create_interview,
)


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

    def get_context_data(self, can_choose_winner=False, **kwargs):
        context = super().get_context_data(**kwargs)
        duel = get_object_or_404(
            Duel.objects.select_related(),
            pk=kwargs.get('duel_id'),
        )
        context['duel_id'] = duel.pk
        context['can_choose_winner'] = can_choose_winner

        context['player1'], context['player2'] = duel.players.all()
        context['duel_question'] = duel.questions.get_no_answered()

        return context

    def _finish_duel(self, context):
        if context.get('duel_question'):
            return self.render_to_response(context)

        return HttpResponseRedirect(
            reverse(
                'interview:duel_finish',
                kwargs={'duel_id': context.get('duel_id')},
            )
        )

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self._finish_duel(context)


class DuelFlowAnsweredView(DuelFlowQuestionView):
    template_name = 'interview/duel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(can_choose_winner=True, **kwargs)
        set_duel_question_is_answered(context.get('duel_question'))

        return context

    def post(self, request, *args, **kwargs):
        duel = get_object_or_404(
            Duel.objects.select_related(),
            pk=kwargs.get('duel_id'),
        )

        duel.players.update_player_and_duel_score(
            winner_pk=int(request.POST.get('duel-radio-player', -1)),
            duel=duel,
        )

        return HttpResponseRedirect(
            reverse(
                'interview:duel',
                kwargs={'duel_id': duel.pk},
            )
        )


class DuelFinishView(TemplateView):
    template_name = 'interview/duel-results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        duel = get_object_or_404(
            Duel.objects.select_related(),
            pk=kwargs.get('duel_id'),
        )

        context['duel'] = duel
        context['player1'], context['player2'] = duel.players.all()

        return context
