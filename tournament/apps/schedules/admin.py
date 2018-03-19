from django.contrib import admin
from tournament.apps.base.admin import BaseAdmin
from tournament.apps.schedules.models import Schedule


# Register your models here.
@admin.register(Schedule)
class ScheduleAdmin(BaseAdmin):
    list_display = (
        'team_local',
        'team_visit',
        'date'
    )
