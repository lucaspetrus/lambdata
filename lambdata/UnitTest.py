# UnitTests for OverwatchCharacters.py in Lambdata


import unittest
from lambdata import OverwatchCharacters


class OverwatchTests(unittest.TestCase):
    """Tests the attributes of Overwatch Characters"""
    def test_health(self):
        """Test to make sure health is 5"""
        person = OverwatchCharacters.Overwatch()
        self.assertEqual(person.health, 5)

    def test_speed(self):
        """Tests to make sure speed is 6"""
        player = OverwatchCharacters.Overwatch()
        self.assertEqual(player.speed, 6)

    def test_damage(self):
        """Tests to make sure speed is 0"""
        player = OverwatchCharacters.Overwatch()
        self.assertEqual(player.damage, 0)


if __name__ == '__main__':
    unittest.main()
