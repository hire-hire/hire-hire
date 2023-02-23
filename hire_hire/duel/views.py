from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from duel.models import Duel

from duel.services import (
    create_duel,
    set_duel_question_is_answered,
)


class DuelSettingsView(TemplateView):
    template_name = 'duel/duel-settings.html'

    def post(self, request, *args, **kwargs):
        duel = create_duel(request)

        return HttpResponseRedirect(
            reverse(
                'duel:duel',
                kwargs={'duel_id': duel.pk},
            )
        )


class DuelFlowQuestionView(TemplateView):
    template_name = 'duel/duel.html'

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
                'duel:duel_finish',
                kwargs={'duel_id': context.get('duel_id')},
            )
        )

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self._finish_duel(context)


class DuelFlowAnsweredView(DuelFlowQuestionView):

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
                'duel:duel',
                kwargs={'duel_id': duel.pk},
            )
        )


class DuelFinishView(TemplateView):
    template_name = 'duel/duel-results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        duel = get_object_or_404(
            Duel.objects.select_related(),
            pk=kwargs.get('duel_id'),
        )

        context['duel'] = duel
        context['player1'], context['player2'] = duel.players.all()

        return context
