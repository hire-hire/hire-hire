from django.conf import settings
from django.contrib import admin
from django.db.models import F, Value
from django.db.models.functions import Concat

from contributors.models import Contributor, ContributorContact


class ContributorContactInline(admin.StackedInline):
    model = ContributorContact
    extra = 1
    max_num = settings.LIMIT_CONTRIBUTORS_CONTACTS


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = (
        Contributor.id.field.name,
        'full_name',
        Contributor.role.field.name,
    )
    list_filter = ('role',)
    inlines = (ContributorContactInline,)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if 'changelist' in request.resolver_match.url_name:
            queryset = queryset.annotate(
                full_name=Concat(
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
        ordering='full_name',
    )
    def full_name(self, obj):
        return obj.full_name
