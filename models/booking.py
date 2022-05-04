
"""
Bookings:-
    -Source
    - Destinations
   - Car_type
  - Driver
 - status:- completed,progress,started

"""


class Booking(object):
    def __init__(self):
        self.source=(None,None)
        self.destination=(None,None)
        self.user=None
        self.driver=None
        self.booking_status=None
        self.price=None


    def set_source(self,source):
        self.source = source

    def get_source(self):
        return self.source


    def set_user(self,user):
        self.user = user

    def get_user(self):
        return self.user

    def set_driver(self,driver):
        self.driver = driver

    def get_driver(self):
        return self.driver


    def set_price(self,price):
        self.price = price

    def get_price(self):
        return self.price

    def set_destination(self,destination):
        self.price = destination

    def get_destination(self):
        return self.destination
    def set_booking_status(self,booking_status):
        self.booking_status = booking_status

    def get_booking_status(self):
        return self.booking_status

