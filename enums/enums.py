import enum
class DriverVerification(enum.Enum):
    VERIFIED, UNVERIFIED=1,0


class CarType(enum.Enum):
    MINI, SUV, SEDAN, UNKNOWN=1,2,3,0

class BookingStatus(enum.Enum):
     STARTED, IN_PROGRESS, CONFIRMED= 1,2,3



class BookedStatus(enum.Enum):
     BOOKED, AVAILABLE= 1,0