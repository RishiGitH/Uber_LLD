

class DriverController():
    def __init__(self, driver_service):
        self.driver_service=driver_service

    def createDriver(self, id, name, rating, cordinate_1,cordinate_2,
                      acceptable_radius,car_type,verification_status,booked_status):
        return self.driver_service.addDriver(id, name, rating, cordinate_1,cordinate_2,
                                      acceptable_radius,car_type,verification_status,booked_status)

