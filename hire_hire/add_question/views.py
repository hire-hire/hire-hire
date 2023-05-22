from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from add_question.forms import AddQuestionForm
from add_question.mixins import GetOrSetUserCookieIdMixin
from add_question.models import AddQuestion
from add_question.services import get_count_questions_text


class AddQuestionMixin(GetOrSetUserCookieIdMixin):
    limit_add_questions_per_day = settings.LIMIT_ADD_QUESTIONS_PER_DAY

    def dispatch(self, request, *args, **kwargs):
        self.add_questions_for24_count = (
            AddQuestion.objects.get_24_hours_added_question_count(
                request.user,
                request.COOKIES.get(AddQuestion.user_cookie_id.field.name),
            )
        )
        response = self.get_or_set_user_cookie_id(
            request,
            super().dispatch,
            *args,
            **kwargs,
        )
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['added_questions'] = get_count_questions_text(
            self.add_questions_for24_count,
        )
        context[
            'limit_add_questions_per_day'
        ] = self.limit_add_questions_per_day
        return context


class AddQuestionView(AddQuestionMixin, CreateView):
    success_url = reverse_lazy('add_question:finished')
    form_class = AddQuestionForm
    template_name = 'add_question/add_question.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['add_questions_for24_count'] = self.add_questions_for24_count
        initial[
            'limit_add_questions_per_day'
        ] = self.limit_add_questions_per_day
        return initial

    def form_valid(self, form):
        form.instance.ip_address = self.request.META.get('REMOTE_ADDR')
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        else:
            form.instance.user_cookie_id = self.user_cookie_id
        return super().form_valid(form)


class AddQuestionFinishView(AddQuestionMixin, TemplateView):
    template_name = 'add_question/add_question-finished.html'
