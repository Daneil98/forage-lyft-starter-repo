import unittest 
from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    
    def test_needs_service_true(self):
        last_service_mileage = 0
        current_service_mileage = 3520
        engine = CapuletEngine(current_service_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
        
    def test_needs_service_false(self):
        last_service_mileage = 0
        current_service_mileage = 3000
        engine = CapuletEngine(current_service_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
        
if __name__ == '__main__':
    unittest.main()