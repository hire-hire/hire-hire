from django.contrib import admin
from static_info.models import TeamRole


@admin.register(TeamRole)
class TeamRoleAdmin(admin.ModelAdmin):
    pass
