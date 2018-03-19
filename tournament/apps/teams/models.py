from django.db import models
from tournament.apps.base.models import BaseModel


# Create your models here.
class Team(BaseModel):
    name = models.CharField(
        max_length=100,
    )
    logo = models.ImageField(
        upload_to='media/team/logo/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
