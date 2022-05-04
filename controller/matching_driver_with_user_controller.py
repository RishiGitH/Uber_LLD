from enums.enums import  BookedStatus
from services.servicelayer.matching_service import MatchingService

class MatchingDriverRiderController():
    def __init__(self, driver_service):
        self.driver_service=driver_service




    def find_driver_for_given_user(self, user, car_type):

        print(car_type)
        list_drivers=self.driver_service.getAllDriverWithCarType(car_type)

        assigned_driver = MatchingService().getDriverMatchService(list_drivers,user)

        assigned_driver.set_booked_status(BookedStatus.BOOKED)

        return assigned_driver