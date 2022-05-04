from ..interfaces.booking_service_interface import BookingServiceInterface
from models.booking import Booking


class BookingService(BookingServiceInterface):
    BookingList = []

    def addBooking(self,source,destination,user,driver,booking_status,price):
        booking = Booking()
        booking.set_source(source)
        booking.set_destination(destination)
        booking.set_user(user)
        booking.set_driver(driver)
        booking.set_booking_status(booking_status)
        booking.set_price(price)

        self.__class__.BookingList.append(booking)

        return booking