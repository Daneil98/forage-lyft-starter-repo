import datetime

class Battery():
    
    def needs_service(self):
        return self.current_date - self.last_service_date > 2
        #2 is the number of years required for servicing