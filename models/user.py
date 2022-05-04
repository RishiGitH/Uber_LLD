from .account import Account


class User(Account):
    def __init__(self):
        self.total_bookings = 0

    def incr_total_bookings(self):
        self.total_bookings += 1

    def get_total_bookings(self):
        return self.total_bookings
