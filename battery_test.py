import unittest
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class TestBattery(unittest.TestCase):
    last_service_date = 2020
    current_date = 2023
    def test_service(self):
        result = SpindlerBattery.needs_service(self)
        self.assertTrue
 