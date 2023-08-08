import unittest
from tyre.carrigan_tyre import CarriganTyre


class TestCarriganTyre(unittest.TestCase):
    def test_needs_service_true(self):
        tyre_wear = [0.1, 0.3, 0.2, 0.9]
        tyre = CarriganTyre(tyre_wear)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        tyre_wear = [0.1, 0.2, 0.4, 0.2]
        tyre = CarriganTyre(tyre_wear)
        self.assertFalse(tyre.needs_service())