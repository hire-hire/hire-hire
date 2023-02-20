__all__ = ['OurTeamAdmin']
from django.contrib import admin

from static_info.models import OurTeam


@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    pass
