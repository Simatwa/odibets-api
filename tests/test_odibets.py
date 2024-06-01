import unittest
from odibets_api import Odibets
import odibets_api.models as models


class TestOdibets(unittest.TestCase):

    def setUp(self):
        self.bet = Odibets()

    def test_daily_jackpot(self):
        self.assertIsInstance(self.bet.daily_jackpot(), models.JackpotMatches)


if __name__ == "__main__":
    unittest.main()
