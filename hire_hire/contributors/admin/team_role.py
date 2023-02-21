from django.contrib import admin

from contributors.models import TeamRole


@admin.register(TeamRole)
class TeamRoleAdmin(admin.ModelAdmin):
    pass
