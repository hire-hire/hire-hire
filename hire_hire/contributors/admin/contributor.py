from django.contrib import admin
from django.db.models import F, Value
from django.db.models.functions import Concat

from contributors.models import ContributorContact, Contributor


class ContributorContactInline(admin.StackedInline):
    model = ContributorContact
    extra = 1


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'role']
    list_filter = ['role']
    inlines = [ContributorContactInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if 'changelist' in request.resolver_match.url_name:
            queryset = queryset.annotate(
                fio=Concat(
                    F('first_name'),
                    Value(' '),
                    F('last_name'),
                    Value(' '),
                    F('middle_name'),
                )
            )
        return queryset

    @admin.display(
        description='фио',
        ordering='fio',
    )
    def fio(self, obj):
        return obj.fio
