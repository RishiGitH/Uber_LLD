import abc
class DriverServiceInterface(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def addDriver(self,id,name,rating, cordinate_1,cordinate_2,acceptable_radius,car_type,verification_status,booked_status):
		pass