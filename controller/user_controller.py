


class UserController():
    def __init__(self, user_service):
        self.user_service=user_service

    def createUser(self, id, name, rating, cordinate_1,cordinate_2):
        # print(cordinate_1,cordinate_2)
        return self.user_service.addUser(id=id, name=name, rating=rating, cordinate_1=cordinate_1,cordinate_2=cordinate_2)

