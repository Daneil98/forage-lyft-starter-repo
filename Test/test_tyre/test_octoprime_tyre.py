import unittest
from tyre.octoprime_tyre import OctoprimeTyre


class TestOctoprimeTyreTyre(unittest.TestCase):
    def test_needs_service_true(self):
        tyre_wear = [0.8, 0.8, 0.8, 0.7]
        tyre = OctoprimeTyre(tyre_wear)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        tyre_wear = [0.1, 0.2, 0.4, 0.2]
        tyre = OctoprimeTyre(tyre_wear)
        self.assertFalse(tyre.needs_service())