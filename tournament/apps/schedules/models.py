from django.db import models
from tournament.apps.base.models import BaseModel
from tournament.apps.teams.models import Team
from django.utils.translation import ugettext as _


# Create your models here.
class Schedule(BaseModel):
    team_local = models.ForeignKey(
        Team,
        related_name='team_local_schedule',
        verbose_name=_('local'),
    )
    team_visit = models.ForeignKey(
        Team,
        related_name='team_visit_schedule',
        verbose_name=_('visit'),
    )
    date = models.DateTimeField(
        null = True,
        blank = True
    )
