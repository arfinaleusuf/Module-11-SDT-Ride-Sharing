
from datetime import datetime
from vehicle import Car, Bike

class RideSharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
    def add_rider(self, rider):
        self.riders.append(rider)
    def add_driver(self, driver):
        self.drivers.append(driver)
    def __repr__(self):
        return f'Company Name {self.company_name} with Riders : {len(self.riders)} and Drivers : {len(self.drivers)}'

class Ride:
    def __init__(self, start_location, end_location, vehicle):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None
        self.vehicle = vehicle

    def set_driver(self, driver):
        self.driver = driver
        
    def start_ride(self):
        self.start_time = datetime.now()
    def end_ride(self):
        self.end_time = datetime.mow()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self):
        return f"ride details. Started {self.start_location} to {self.end_location}"
    
"""
rider request e ki ki thake
    1. ke request korche --rider
    2. se kothay jane --end location
"""

class RideRequest:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location

class RideMatching:
    def __init__(self, drivers):
        self.available_drivers = drivers

    def find_drivers(self, ride_request, vehicle_type):
        if len(self.available_drivers) > 0:
            print("Locking for drivers...")
            driver = self.available_drivers[0]
            
            if vehicle_type == 'car':
                vehicle = Car('car', 'abc456', 30)
            elif vehicle_type == 'bike':
                vehicle = Bike('Motor bike', '1235bh', 50)
            ride = Ride(ride_request.rider.current_location, ride_request.end_location, vehicle)

            driver.accept_ride(ride)
            return ride