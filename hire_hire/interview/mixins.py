from django.http import HttpResponseRedirect
from django.urls import reverse


class CheckDuelFinishMixin:
    """Проверка на то, что если у нас в контексте нет duel_question - то редиректит на финиш дуэли"""

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
