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
        'pub_date', 'author'
        )
    search_fields = ('language', 'text', 'answer')
    list_filter = ('language', 'status')
    empty_value_display = '-пусто-'

    readonly_fields = ('status', 'ip_address', 'author', 'approve_button',
                       'reject_button')
    actions = ('approve', 'reject')

    def approve(self, request, queryset):
        questions = [
            Question(language=obj.language, text=obj.text, answer=obj.answer, )
            for obj in queryset]
        Question.objects.bulk_create(questions)
        queryset.update(status='approved')
        self.message_user(request, f'Одобрено {len(questions)} вопроса.')

    approve.short_description = 'Одобрить выбранные вопросы'

    def reject(self, request, queryset):
        queryset.update(status='rejected')
        self.message_user(request, f'Отклонено {len(queryset)} вопроса.')

    reject.short_description = 'Отклонить выбранные вопросы'

    def response_change(self, request, obj):
        if self.APPROVE in request.POST:
            Question.objects.create(
                language=obj.language,
                text=obj.text,
                answer=obj.answer,
                )
            # obj.delete()
            obj.status = 'approved'
            obj.save()
            self.message_user(request, 'Вопрос одобрен.')
            return HttpResponseRedirect(
                reverse('admin:add_question_addquestion_changelist'))
        if self.REJECT in request.POST:
            obj.status = 'rejected'
            obj.save()
            self.message_user(request, 'Вопрос отклонён.')
            return HttpResponseRedirect(
                reverse('admin:add_question_addquestion_changelist'))
        return super().response_change(request, obj)

    def approve_button(self, obj):
        return mark_safe(
            '<div class="submit-row">'
            f'<input type="submit" value="ОДОБРИТЬ" name={self.APPROVE}>'
            '</div>')

    approve_button.short_description = 'Одобряем?'

    def reject_button(self, obj):
        return mark_safe(
            '<div class="submit-row">'
            f'<input type="submit" value="ОТКЛОНИТЬ" name={self.REJECT}>'
            '</div>')

    reject_button.short_description = 'Отклонить?'
