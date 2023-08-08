from tyre.tyre import Tyre

class OctoprimeTyre(Tyre):
    def __init__(self, tyre_wear):
        self.tyre_wear = tyre_wear
    
    def needs_service(self):
        if self.tyre_wear >= 0.9:
            return True
        else:
            return False 