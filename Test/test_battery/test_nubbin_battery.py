import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery



class TestNubbinBattery(unittest.TestCase):
    
    def test_needs_service_true(self):
        last_service_date = date.fromisoformat ("2020-07-07")
        current_date = date.fromisoformat("2023-07-07")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
        
    def test_needs_service_false(self):
        last_service_date = date.fromisoformat ("2022-07-07")
        current_date = date.fromisoformat("2023-07-07")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
        
        
if __name__ == '__main__':
    unittest.main()