from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.safestring import mark_safe

from add_question.models import AddQuestion
from interview.models import Question


@admin.register(AddQuestion)
class AddQuestionAdmin(admin.ModelAdmin):
    """Админ панель предложенных вопросов."""
    list_display = (
        'pk', 'rejected', 'language', 'text', 'answer', 'ip_address',
        'pub_date', 'author'
        )
    search_fields = ('language', 'text', 'answer')
    list_filter = ('language', 'rejected')
    empty_value_display = '-пусто-'

    readonly_fields = ('ip_address', 'author', 'custom_button',
                       )  # 'reject_button'
    actions = ('approve', )

    def approve(self, request, queryset):
        questions = [
            Question(language=obj.language, text=obj.text, answer=obj.answer, )
            for obj in queryset]
        Question.objects.bulk_create(questions)
        queryset.delete()
        self.message_user(request, f'Одобрено {len(questions)} вопроса.')

    approve.short_description = 'Одобрить выбранные вопросы'

    def response_change(self, request, obj):
        if '_approve' in request.POST:
            Question.objects.create(
                language=obj.language,
                text=obj.text,
                answer=obj.answer,
                )
            obj.delete()
            self.message_user(request, 'Вопрос одобрен.')
            return HttpResponseRedirect(
                reverse('admin:add_question_addquestion_changelist'))
        return super().response_change(request, obj)

    def custom_button(self, obj):
        return mark_safe(
            '<div class="submit-row">'
            '<input type="submit" value="ОДОБРИТЬ" name="_approve"> </div>')

    custom_button.short_description = 'Одобряем?'

    # def reject_button(self, obj):
    #     return mark_safe(
    #         '<div class="submit-row">'
    #         '<input type="submit" value="ОТКЛОНИТЬ" name="_approve"> </div>')

    # reject_button.short_description = 'Отклонить?'
