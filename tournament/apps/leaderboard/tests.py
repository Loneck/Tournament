from django.test import TestCase
from django.core.urlresolvers import reverse
from tournament.apps.leaderboard.models import Leaderboard

# Create your tests here.
class LeaderboardListViewTestCase(TestCase):

    def setUp(self):
        self.resp = self.client.get('/')

    def test_leaderboard_list(self):
        """
        Test Leaderboard View
        """
        self.assertEqual(self.resp.status_code, 200)
