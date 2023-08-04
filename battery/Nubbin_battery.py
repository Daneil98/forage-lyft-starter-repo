from datetime import datetime
from .battery import needs_service

class NubbinBattery():
    def __init__(self, current_date, last_service_date):
        self.current_date = datetime
        self.last_service_date = datetime
    
    def needs_service(self):
        return self.current_date - self.last_service_date > 4