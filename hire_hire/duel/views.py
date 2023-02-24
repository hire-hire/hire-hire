from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from duel.models import Duel
from duel.services import create_duel, set_duel_question_is_answered


class DuelSettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'duel/duel-settings.html'

    def dispatch(self, request, *args, **kwargs):
        user = request.user

        if user.is_authenticated and not user.is_duel_moderator:
            return HttpResponseRedirect(reverse('homepage:index'))

        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        duel = create_duel(request)

        return HttpResponseRedirect(
            reverse(
                'duel:duel',
                kwargs={'duel_id': duel.pk},
            )
        )


class DuelFlowQuestionView(LoginRequiredMixin, TemplateView):
    template_name = 'duel/duel.html'

    def get_context_data(self, duel_id, can_choose_winner=False, **kwargs):
        context = super().get_context_data(**kwargs)
        duel = Duel.objects.get_duel_by_user(
            duel_pk=duel_id,
            user=self.request.user,
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
        return context

    def post(self, request, duel_id, *args, **kwargs):
        duel = Duel.objects.get_duel_by_user(
            duel_pk=duel_id,
            user=self.request.user,
        )

        no_answered_questions = duel.questions.get_no_answered()
        if no_answered_questions:
            set_duel_question_is_answered(no_answered_questions)
            duel.players.update_player_and_duel_score(
                winner_pk=int(request.POST.get('duel-radio-player', -1)),
                duel=duel,
            )

        return HttpResponseRedirect(
            reverse(
                'duel:duel',
                kwargs={'duel_id': duel_id},
            )
        )


class DuelFinishView(LoginRequiredMixin, TemplateView):
    template_name = 'duel/duel-results.html'

    def get_context_data(self, duel, **kwargs):
        context = super().get_context_data(**kwargs)

        context['duel'] = duel
        context['player1'], context['player2'] = duel.players.all()

        return context

    def get(self, request, duel_id, *args, **kwargs):
        duel = Duel.objects.get_duel_by_user(
            duel_pk=duel_id,
            user=self.request.user,
        )
        if duel.questions.get_no_answered():
            return HttpResponseRedirect(reverse('duel:duel', args=(duel_id,)))

        context = self.get_context_data(duel, **kwargs)
        return self.render_to_response(context)
