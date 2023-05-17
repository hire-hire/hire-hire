from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.safestring import mark_safe

from add_question.mixins import DefaultFilterMixin
from add_question.models import AddQuestion
from add_question.services import count_questions_text
from interview.models import Question


@admin.register(AddQuestion)
class AddQuestionAdmin(DefaultFilterMixin, admin.ModelAdmin):
    """Админ панель предложенных вопросов."""

    APPROVE = '_approve'
    REJECT = '_reject'

    list_display = (
        AddQuestion.id.field.name,
        AddQuestion.status.field.name,
        AddQuestion.language.field.name,
        AddQuestion.text.field.name,
        AddQuestion.answer.field.name,
        AddQuestion.ip_address.field.name,
        AddQuestion.pub_date.field.name,
        AddQuestion.author.field.name,
    )
    search_fields = (
        AddQuestion.language.field.name,
        AddQuestion.text.field.name,
        AddQuestion.answer.field.name,
    )
    list_filter = (
        AddQuestion.language.field.name,
        AddQuestion.status.field.name,
    )
    default_filters = (('status__exact', AddQuestion.StatusChoice.PROPOSED),)
    empty_value_display = '-пусто-'

    readonly_fields = (
        AddQuestion.status.field.name,
        AddQuestion.ip_address.field.name,
        AddQuestion.user_cookie_id.field.name,
        AddQuestion.author.field.name,
        'approve_button',
        'reject_button',
    )
    actions = ('approve', 'reject')

    def approve(self, request, queryset):
        questions = [
            Question(language=obj.language, text=obj.text, answer=obj.answer)
            for obj in queryset
        ]
        Question.objects.bulk_create(questions)
        queryset.update(status=AddQuestion.StatusChoice.APPROVED)
        self.message_user(
            request,
            f'Одобрен{count_questions_text(len(questions))}.',
        )

    approve.short_description = 'Одобрить выбранные вопросы'

    def reject(self, request, queryset):
        queryset.update(status=AddQuestion.StatusChoice.REJECTED)
        self.message_user(
            request,
            f'Отклонен{count_questions_text(len(queryset))}.',
        )

    reject.short_description = 'Отклонить выбранные вопросы'

    def response_change(self, request, obj):
        if request.POST.get('status') == self.APPROVE:
            Question.objects.create(
                language=obj.language,
                text=obj.text,
                answer=obj.answer,
            )
            obj.status = AddQuestion.StatusChoice.APPROVED
            obj.save()
            self.message_user(request, 'Вопрос одобрен.')
            return HttpResponseRedirect(
                reverse('admin:add_question_addquestion_changelist')
            )
        elif request.POST.get('status') == self.REJECT:
            obj.status = AddQuestion.StatusChoice.REJECTED
            obj.save()
            self.message_user(request, 'Вопрос отклонён.')
            return HttpResponseRedirect(
                reverse('admin:add_question_addquestion_changelist')
            )
        return super().response_change(request, obj)

    def approve_button(self, obj):
        return mark_safe(
            '<div class="submit-row">'
            f'<button type="submit" value={self.APPROVE} name="status">'
            'ОДОБРИТЬ</button></div>'
        )

    approve_button.short_description = 'Одобряем?'

    def reject_button(self, obj):
        return mark_safe(
            '<div class="submit-row">'
            f'<button type="submit" value={self.REJECT} name="status">'
            'ОТКЛОНИТЬ</button></div>'
        )

    reject_button.short_description = 'Отклонить?'
