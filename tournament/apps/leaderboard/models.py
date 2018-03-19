from django.db import models
from tournament.apps.base.models import BaseModel
from tournament.apps.teams.models import Team


# Create your models here.
class Leaderboard(BaseModel):
    team = models.OneToOneField(
        Team,
        related_name='team_leaderboard',
        null=True
    )
    points = models.IntegerField(
        default=0
    )
    win = models.IntegerField(
        default=0
    )
    lose = models.IntegerField(
        default=0
    )
    tie = models.IntegerField(
        default=0
    )

    def __str__(self):
        return self.team.name
