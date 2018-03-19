from django.shortcuts import render
from django.views.generic import ListView
from tournament.apps.leaderboard.models import Leaderboard

# Create your views here.
class LeaderboardList(ListView):
    model = Leaderboard
