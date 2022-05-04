
from configs.price_configs import DISTANCE_PER_UNIT_COST,CAR_TYPE_PRICE_COST, SURGE_FACTOR_MULTIPLE
from enums.enums import CarType

class PriceController():
    def __init__(self, mapping_service, booking_service):
        self.mapping_service=mapping_service
        self.booking_service=booking_service

    def get_ride_estimation(self, source, destination , car_type):
        price_cost=0
        distance_ride = self.mapping_service.cal_euclidian_distance_between_two_points(source, destination)
        print("distance of ride ", distance_ride)

        price_cost+= distance_ride*DISTANCE_PER_UNIT_COST
        car_type_cost = CAR_TYPE_PRICE_COST.get(car_type)

        price_cost += car_type_cost
        number_bookings = len(self.booking_service.BookingList)
        surge_cost = number_bookings % SURGE_FACTOR_MULTIPLE

        price_cost+= surge_cost

        return price_cost





