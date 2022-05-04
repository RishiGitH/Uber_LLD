from .account import Account
from enums.enums import  DriverVerification,CarType,BookedStatus
from configs.driver_configs import DEFAULT_ACCEPTABLE_RADIUS

class Driver(Account):
    def __init__(self):
        self.verification_status=DriverVerification.UNVERIFIED
        self.acceptable_radius=DEFAULT_ACCEPTABLE_RADIUS
        self.car_type = CarType.UNKNOWN
        self.booked_status=BookedStatus.AVAILABLE


    def set_verification_status(self,verification_status):
        self.verification_status = verification_status

    def get_verification_status(self):
        return self.verification_status

    def set_acceptable_radius(self,acceptable_radius):
        self.acceptable_radius = acceptable_radius

    def get_acceptable_radius(self):
        return self.acceptable_radius


    def set_car_type(self,car_type):
        self.car_type = car_type

    def get_car_type(self):
        return self.car_type

    def set_booked_status(self,booked_status):
        self.booked_status = booked_status

    def get_booked_status(self):
        return self.booked_status


