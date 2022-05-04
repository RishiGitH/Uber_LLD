from .map_service import MapService

class MatchingService(object):


    def getDriverMatchService(self, list_drivers, user):
        print(list_drivers)
        for driver in list_drivers:
            user_location=user.get_location()
            driver_location = driver.get_location()
            distance_bw_user_driver = MapService().cal_euclidian_distance_between_two_points\
                (user_location,driver_location)
            # print(distance_bw_user_driver)
            if distance_bw_user_driver<= driver.get_acceptable_radius():
                return driver

        return None
