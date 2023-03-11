from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from add_question.forms import AddQuestionForm
from add_question.models import AddQuestion


class AddQuestionMixin:
    limit_add_questions_per_day = getattr(
        settings, 'LIMIT_ADD_QUESTIONS_PER_DAY', 10)

    def dispatch(self, request, *args, **kwargs):
        self.add_questions_for24_count = (
            AddQuestion.objects.get_24_hours_added_question(request))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['added_questions'] = self.add_questions_for24_count
        context['limit_add_questions_per_day'] = (
            self.limit_add_questions_per_day)
        return context


class AddQuestionView(AddQuestionMixin, CreateView):
    success_url = reverse_lazy('add_question:finished')
    form_class = AddQuestionForm
    template_name = 'add_question/add_question.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['add_questions_for24_count'] = self.add_questions_for24_count
        initial['limit_add_questions_per_day'] = (
            self.limit_add_questions_per_day)
        return initial

    def form_valid(self, form):
        form.instance.ip_address = self.request.META.get('REMOTE_ADDR')
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        return super().form_valid(form)


class AddQuestionFinishView(AddQuestionMixin, TemplateView):
    template_name = 'add_question/add_question-finished.html'