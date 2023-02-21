from django.contrib import admin

from .models import Language, Question


class LanguageAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Language, LanguageAdmin)
admin.site.register(Question, QuestionAdmin)
