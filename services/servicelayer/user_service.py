from ..interfaces.user_service_interface import UserServiceInterface
from models.user import User


class UserService(UserServiceInterface):
    userDetails = {}

    def addUser(self, id, name, rating, cordinate_1, cordinate_2):
        user = User()
        user.set_id(id)
        user.set_name(name)
        user.set_rating(rating)
        user.set_location(cordinate_1, cordinate_2)
        self.__class__.userDetails[id] = user
        return user