from django.test import TestCase
from tournament.apps.schedules.models import Schedule
from tournament.apps.teams.models import Team


# Create your tests here.
class ScheduleTestCase(TestCase):

    def setUp(self):
        self.team_visit = Team.objects.create(name='Golden State Warrior')
        self.team_local = Team.objects.create(name='Oklahoma City Thunder')

    def test_schedule_create(self):
        """
        Test Schedule Create
        """
        self.assertTrue(Schedule.objects.create(
            team_local=self.team_local,
            team_visit=self.team_visit,
            date='2018-03-19 16:16:31',
        ))
