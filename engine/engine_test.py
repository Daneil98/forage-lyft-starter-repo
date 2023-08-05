import unittest 
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestEngine(unittest.TestCase):
    
    def test_service(self):
        result = CapuletEngine.needs_service(self)
        self.assertTrue
