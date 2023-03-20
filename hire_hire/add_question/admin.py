from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.safestring import mark_safe

from add_question.models import AddQuestion
from interview.models import Question


@admin.register(AddQuestion)
class AddQuestionAdmin(admin.ModelAdmin):
    """Админ панель предложенных вопросов."""
    APPROVE = '_approve'
    REJECT = '_reject'

    list_display = (
        'pk', 'status', 'language', 'text', 'answer', 'ip_address',
        'pub_date', 'author',
    )
    search_fields = ('language', 'text', 'answer')
    list_filter = ('language', 'status')
    empty_value_display = '-пусто-'

    readonly_fields = (
        'status', 'ip_address',  'user_cookie', 'author', 'approve_button',
        'reject_button',
    )
    actions = ('approve', 'reject')

    def count_questions_text(self, count_questions):
        last_digit = count_questions % 10
        if 11 <= count_questions <= 20 or last_digit == 0 or last_digit >= 5:
            return f'о {count_questions} вопросов'
        elif last_digit == 1:
            return f' {count_questions} вопрос'
        else:
            return f'о {count_questions} вопроса'

    def approve(self, request, queryset):
        questions = [
            Question(
                language=obj.language,
                text=obj.text,
                answer=obj.answer
            ) for obj in queryset
        ]
        Question.objects.bulk_create(questions)
        queryset.update(status=AddQuestion.StatusChoice.APPROVED)
        self.message_user(
            request, f'Одобрен{self.count_questions_text(len(questions))}.'
        )

    approve.short_description = 'Одобрить выбранные вопросы'

    def reject(self, request, queryset):
        queryset.update(status=AddQuestion.StatusChoice.REJECTED)
        self.message_user(
            request, f'Отклонен{self.count_questions_text(len(queryset))}.'
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
                reverse('admin:add_question_addquestion_changelist'))
        elif request.POST.get('status') == self.REJECT:
            obj.status = AddQuestion.StatusChoice.REJECTED
            obj.save()
            self.message_user(request, 'Вопрос отклонён.')
            return HttpResponseRedirect(
                reverse('admin:add_question_addquestion_changelist'))
        return super().response_change(request, obj)

    def approve_button(self, obj):
        return mark_safe(
            '<div class="submit-row">'
            f'<button type="submit" value={self.APPROVE} name="status">'
            'ОДОБРИТЬ</button></div>')

    approve_button.short_description = 'Одобряем?'

    def reject_button(self, obj):
        return mark_safe(
            '<div class="submit-row">'
            f'<button type="submit" value={self.REJECT} name="status">'
            'ОТКЛОНИТЬ</button></div>')

    reject_button.short_description = 'Отклонить?'
