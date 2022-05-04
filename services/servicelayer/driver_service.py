from ..interfaces.driver_service_interface import DriverServiceInterface
from models.driver import Driver
from enums.enums import  BookedStatus


class DriverService(DriverServiceInterface):
    driverDetails = {}

    def addDriver(self, id, name, rating, cordinate_1,cordinate_2,acceptable_radius,car_type,verification_status,booked_status):
        driver = Driver()
        driver.set_id(id)
        driver.set_name(name)
        driver.set_rating(rating)
        driver.set_location(cordinate_1, cordinate_2)
        driver.set_acceptable_radius(acceptable_radius)
        driver.set_car_type(car_type)
        driver.set_verification_status(verification_status)
        driver.set_booked_status(booked_status)

        self.__class__.driverDetails[id] = driver
        
        return driver

    def getAllDriverWithCarType(self, car_type):

        list_drivers=[]
        for driver_id in self.__class__.driverDetails.keys():
            driver= self.__class__.driverDetails[driver_id]
            # print(driver , driver.__dict__,driver.car_type.value, car_type,driver.car_type.value,driver.booked_status,BookedStatus.AVAILABLE.value )
            if driver.booked_status==BookedStatus.AVAILABLE.value and driver.car_type.value==car_type:
                list_drivers.append(driver)

        return list_drivers


