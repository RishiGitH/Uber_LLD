from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self):
        self.id=None
        self.name=None
        self.rating=None
        self.location=(None,None)

    def set_id(self,id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name


    def set_rating(self,rating):
        self.rating = rating

    def get_rating(self):
        return self.rating

    def set_location(self, cordinate_1, cordinate_2):
        self.location = (cordinate_1, cordinate_2)

    def get_location(self):
        return self.location


