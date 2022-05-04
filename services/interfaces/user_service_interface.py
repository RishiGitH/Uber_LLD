import abc
class UserServiceInterface(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def addUser(self,id,name,rating, cordinate_1, cordinate_2):
		pass