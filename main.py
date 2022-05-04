import sys,os
sys.path.append(os.getcwd())

from controller.driver_controller import DriverController
from controller.user_controller import UserController
from controller.booking_controller import BookingController
from controller.price_controller import PriceController
from controller.matching_driver_with_user_controller import MatchingDriverRiderController

from enums.enums import  CarType,BookingStatus
from services.servicelayer.booking_service import BookingService
from services.servicelayer.user_service import UserService
from services.servicelayer.map_service import MapService
from services.servicelayer.matching_service import MatchingService
from services.servicelayer.driver_service import DriverService


driver_serive=DriverService()
booking_Service = BookingService()
driverController = DriverController(driver_serive)
userController = UserController(UserService())
priceController = PriceController(MapService(),booking_Service)
bookingController = BookingController(booking_Service)
matchingDriverRiderController = MatchingDriverRiderController(driver_serive)

#addUser(self, id, name, rating, cordinate_1,cordinate_2):
user1 = userController.createUser(id=1, name="test1", rating=5, cordinate_1=4,cordinate_2=5)
user2 = userController.createUser(2, "test2", 5,4,5)
user3 = userController.createUser(3, "test3", 5,4,5)

#    def addDriver(self, id, name, rating, cordinate_1,cordinate_2,acceptable_radius,car_type,verification_status,booked_status):

driver1 = driverController.createDriver(6, "test6", 5, 7,  10,20,CarType.MINI,1,0)
driver2 = driverController.createDriver(4, "test4", 5, 7,10,20,CarType.SEDAN,1,0)
driver3 = driverController.createDriver(5, "test5", 5, 7,10,20,CarType.SUV,1,0)

# get_ride_estimation(self, source, destination , car_type):
price_ride_1 = priceController.get_ride_estimation((3,4),(5,6),1)


print("price ride 1", price_ride_1)
driver_assigned_1 = matchingDriverRiderController.find_driver_for_given_user(user1,1 )

print("driver_assigned_1", driver_assigned_1)
#    def createBooking(self, source,destination,user,driver,booking_status,price):
booking_1 = bookingController.createBooking((3,4),(5,6),user1,driver_assigned_1,BookingStatus.STARTED,price_ride_1)

print("booking_1", booking_1)



price_ride_2 = priceController.get_ride_estimation((4,8),(9,10),2)


print("price_ride_2",price_ride_2)
driver_assigned_2 = matchingDriverRiderController.find_driver_for_given_user(user2,2)

print("driver_assigned_2",driver_assigned_2)
booking_2 = bookingController.createBooking((4,8),(9,10),user1,driver_assigned_2,BookingStatus.STARTED,price_ride_2)

print("booking_2",booking_2)

print(BookingService.BookingList, len(BookingService.BookingList))





