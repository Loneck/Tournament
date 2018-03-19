from django.contrib import admin
from tournament.apps.base.admin import BaseAdmin
from tournament.apps.results.models import Result


# Register your models here.
@admin.register(Result)
class ResultAdmin(BaseAdmin):
    list_display = (
        'match',
        'team_local_score',
        'team_visit_score',
    )
