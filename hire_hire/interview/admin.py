from django.contrib import admin

from interview.models import Category, Language, Question, QuestionAnswer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


class QuestionAnswerInline(admin.StackedInline):
    model = QuestionAnswer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (QuestionAnswerInline,)
