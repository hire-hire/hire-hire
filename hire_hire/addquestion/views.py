from django.db.models import Q
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, TemplateView

from hire_hire.settings import MAX_ADDQUESTIONS_PER_DAY
from .forms import AddQuestionForm
from .models import AddQuestion


class AddQuestionMixin:
    def dispatch(self, request, *args, **kwargs):
        ago_24_hours = timezone.now() - timezone.timedelta(hours=24)
        self.current_ip_address = request.META.get('REMOTE_ADDR')
        self.addquestions_for24_count = (
            AddQuestion.objects
            .filter(Q(pub_date__gte=ago_24_hours) & Q(
                ip_address=self.current_ip_address))).count()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['added_questions'] = self.addquestions_for24_count
        return context


class AddQuestionView(AddQuestionMixin, CreateView):
    success_url = reverse_lazy('addquestion:finished')
    form_class = AddQuestionForm
    template_name = 'addquestion/addquestion.html'

    def form_valid(self, form):
        form.instance.ip_address = self.request.META.get('REMOTE_ADDR')
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        if self.addquestions_for24_count >= MAX_ADDQUESTIONS_PER_DAY:
            form.add_error(None, 'Вы исчерпали лимит вопросов на день.')
            return super().form_invalid(form)
            # time.sleep(5) # задержка на 5 секунд, шляпа полная
            # return HttpResponseRedirect(reverse('homepage:index'))
        return super().form_valid(form)


class AddQuestionFinishView(AddQuestionMixin, TemplateView):
    template_name = 'addquestion/addquestion-finished.html'
