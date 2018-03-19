from django.test import TestCase
from tournament.apps.teams.models import Team


# Create your tests here.
class TeamTestCase(TestCase):

    def test_team_create(self):
        """
        Test Team Create
        """
        self.assertTrue(Team.objects.create(name='Golden State Warrior'))
        self.assertTrue(Team.objects.create(name='Oklahoma City Thunder'))
