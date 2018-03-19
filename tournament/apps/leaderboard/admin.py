from django.contrib import admin
from tournament.apps.base.admin import BaseAdmin
from tournament.apps.leaderboard.models import Leaderboard


# Register your models here.
@admin.register(Leaderboard)
class LeaderboardAdmin(BaseAdmin):
    list_display = (
        'team',
    )
