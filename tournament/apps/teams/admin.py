from django.contrib import admin
from tournament.apps.base.admin import BaseAdmin
from tournament.apps.teams.models import Team


# Register your models here.
@admin.register(Team)
class TeamAdmin(BaseAdmin):
    list_display = (
        'name',
    )
