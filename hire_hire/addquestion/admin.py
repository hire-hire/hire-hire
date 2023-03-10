from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.safestring import mark_safe

from interview.models import Question
from .models import AddQuestion


@admin.register(AddQuestion)
class AddQuestionAdmin(admin.ModelAdmin):
    """Админ панель предложенных вопросов."""
    list_display = (
        'pk', 'language', 'text', 'answer', 'ip_address', 'pub_date', 'author',
        )
    # list_editable = ('language', )
    search_fields = ('language', 'text', 'answer', )
    list_filter = ('language',)
    empty_value_display = '-пусто-'

    readonly_fields = ('ip_address', 'author', 'custom_button',)
    actions = ['approve', 'appr']

    def approve(self, request, queryset):
        for obj in queryset:
            Question.objects.create(
                language=obj.language,
                text=obj.text,
                answer=obj.answer
            )
            obj.delete()
        self.message_user(request, f'Одобрено {queryset.count()} вопроса.')

    approve.short_description = 'Одобрить выбранные вопросы'

    def response_change(self, request, obj):
        if '_approve' in request.POST:
            Question.objects.create(
                language=obj.language,
                text=obj.text,
                answer=obj.answer
                )
            obj.delete()
            self.message_user(request, 'Вопрос одобрен.')
            return HttpResponseRedirect(
                reverse('admin:addquestion_addquestion_changelist'))  # ('.')
        return super().response_change(request, obj)

    def custom_button(self, obj):
        return mark_safe(
            '<div class="submit-row">'
            '<input type="submit" value="ОДОБРИТЬ" name="_approve"> </div>')

    custom_button.short_description = 'Одобряем?'
