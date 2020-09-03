import unittest
from lambdata import Overwatch




class OverwatchTests(unittest.TestCase):
    """Tests the attributes of Overwatch Characters"""
    def test_health(self):
        person = Overwatch()
        self.assertEqual(person.health, 5)




if __name__ == '__main__':
    unittest.main()
