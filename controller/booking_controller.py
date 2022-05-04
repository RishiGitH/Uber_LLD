

class BookingController():
    def __init__(self, booking_service):
        self.booking_service=booking_service

    def createBooking(self, source,destination,user,driver,booking_status,price):
        return self.booking_service.addBooking(source,destination,user,driver,booking_status,price)


