from django.contrib import admin

from contributors.models import OurTeam


@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    pass
