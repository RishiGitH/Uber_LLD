import abc
class BookingServiceInterface(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def addBooking(self,source,destination,user,driver,booking_status,price):
		pass