from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from duel.models import Duel
from duel.services import create_duel, set_duel_question_is_answered
from duel.forms import DuelSettingsForm, DuelFlowAnsweredForm


class DuelSettingsView(LoginRequiredMixin, FormView):
    template_name = 'duel/duel-settings.html'
    form_class = DuelSettingsForm

    def dispatch(self, request, *args, **kwargs):
        user = request.user

        if user.is_authenticated and not user.is_duel_moderator:
            return HttpResponseRedirect(reverse('homepage:index'))

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        duel = create_duel(
            user=self.request.user,
            question_count=form.cleaned_data['questions_count'],
            players_names=(
                form.cleaned_data['first_player'],
                form.cleaned_data['second_player'],
            ),
        )

        self.success_url = reverse(
            'duel:duel',
            kwargs={'duel_id': duel.pk},
        )
        return super().form_valid(form)


class DuelFlowQuestionView(LoginRequiredMixin, FormView):
    template_name = 'duel/duel.html'
    form_class = DuelFlowAnsweredForm
    duel = None
    duel_players = None

    def get_form_class(self):
        self.duel = Duel.objects.get_duel_by_user(
            duel_pk=self.kwargs.get('duel_id'),
            user=self.request.user,
        )
        self.duel_players = self.duel.players.all()

        return super().get_form_class()

    def get_form_kwargs(self, can_choose_winner=False):
        kwargs = super().get_form_kwargs()

        kwargs['players'] = (
            *[(player.pk, player.name) for player in self.duel_players],
            [-1, 'Нет правильного ответа']
        )

        kwargs['can_choose_winner'] = can_choose_winner
        return kwargs

    def get_context_data(self, duel_id, can_choose_winner=False, **kwargs):
        context = super().get_context_data(**kwargs)

        context['duel_id'] = self.duel.pk
        context['can_choose_winner'] = can_choose_winner

        context['player1'], context['player2'] = self.duel_players
        context['duel_question'] = self.duel.questions.get_no_answered()

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
        context = self.get_context_data(*args, **kwargs)
        return self._finish_duel(context)


class DuelFlowAnsweredView(DuelFlowQuestionView):

    def get_form_kwargs(self):
        return super().get_form_kwargs(can_choose_winner=True)

    def form_valid(self, form):
        no_answered_question = self.duel.questions.get_no_answered()
        if no_answered_question:
            set_duel_question_is_answered(no_answered_question)
            self.duel.players.update_player_and_duel_score(
                winner_pk=form.cleaned_data['player_pk'],
                duel=self.duel,
            )

        self.success_url = reverse(
            'duel:duel',
            kwargs={'duel_id': self.duel.pk},
        )
        return super().form_valid(form)

    def get_context_data(self, duel_id, can_choose_winner=False, **kwargs):
        return super().get_context_data(
            duel_id,
            can_choose_winner=True,
            **kwargs,
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
