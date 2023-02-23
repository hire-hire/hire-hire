from django.contrib import admin

from interview.models import Language, Question


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


