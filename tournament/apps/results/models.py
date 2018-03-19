from django.db import models
from tournament.apps.base.models import BaseModel
from tournament.apps.schedules.models import Schedule
from django.utils.translation import ugettext as _


# Create your models here.
class Result(BaseModel):
    match = models.ForeignKey(
        Schedule,
        related_name='match_result',
        verbose_name=_('match'),
    )
    team_local_score = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    team_visit_score = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return 'L %s - %s V' %(self.team_local_score,self.team_visit_score)
