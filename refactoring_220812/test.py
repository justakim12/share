from unittest import TestCase

from refactoring_220812.version4.main import activate


class RefactorTest(TestCase):
    def test_activate(self):
        region = "kr"
        env = "qa"
        region_timezone, city_name, threshold = activate(region, env)
        expected = region_timezone, city_name, threshold
        actual = "KST", "Seoul", 20
        self.assertEqual(expected, actual)