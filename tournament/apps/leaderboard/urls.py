# -*- coding: utf-8 -*-
from django.conf.urls import url
from tournament.apps.leaderboard.views import LeaderboardList

urlpatterns = [
    url(r'^$', LeaderboardList.as_view(), name='leaderboard'),
]
