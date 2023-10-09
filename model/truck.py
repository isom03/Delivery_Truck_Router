# Class for delivery trucks
from datetime import timedelta
from model.locationDistances import distance_between_addresses


class DeliveryTruck:

    # Constructor for truck object
    def __init__(self):
        self.manifest = []
        self.distance_traveled = 0
        self.current_time = timedelta(hours=8)
        self.current_location = "4001 South 700 East"

    # Functions allow me to manipulate variables/fields associated with a specific instance of a truck
    def add_package(self, package):
        self.manifest.append(package)

    def package_delivered(self, package):
        self.manifest.remove(package)

    def get_truck_time(self):
        return self.current_time

    def get_distance_traveled(self):
        return self.distance_traveled

    def add_distance(self, distance):
        self.distance_traveled = self.distance_traveled + distance

    def add_time(self, time_to_deliver):
        the_time = timedelta(hours=time_to_deliver)
        self.current_time = self.current_time + the_time

    def set_time(self, new_time):
        self.current_time = new_time

    def get_location(self):
        return self.current_location

    def set_current_location(self, address):
        self.current_location = address

    """
        next_package_to_deliver():
            Function/Method determines the nearest address to the trucks location based off the
            trucks manifest (list of packages)

        Args:
            self: the truck the function is be called on
            locations: the list of possible delivery locations and the distances between locations.
            It is primarily used to get distances between locations

        Returns:
            next_package_to_deliver: Returns the package with the delivery address closest to the truck's current location

        Raises:
            N/A: This function raises no errors/has no error checking

        Time complexity:
            The time complexity of this function is O(N)

        Space complexity:
            The space complexity is also O(N)
    """
    def next_package_to_deliver(self, locations):
        # Initializing shortest_distance variable to unrealistic distance for first comparison
        shortest_distance = 1000

        # Going through each package in a trucks manifest using for loop
        for some_package in self.manifest:
            # temp_address stores address of current package being looked at in for loop.
            # will be used to calculated possible route for truck
            temp_address = some_package.get_address()
            # distance
            possible_route = float(distance_between_addresses(self.get_location(), temp_address, locations))
            # If the new possible route is shorter than the previous route, then the next_package_to_deliver is set
            # to the current package being looked at in for loop
            if possible_route < shortest_distance:
                next_package_to_deliver = some_package
                shortest_distance = possible_route
        # After all possible routes have been looked at, the package which has the shortest (or closest) possible route
        # is returned.
        return next_package_to_deliver

    # Function to calculate amount time past in hours based on distance traveled by truck
    def time_to_deliver(self, distance_traveled):
        time_in_hours = distance_traveled / 18
        return time_in_hours

    # Manually loading truck #1 for first delivery route
    def load_truck_one(self, the_hash_table):
        self.add_package(the_hash_table.get(1))
        self.add_package(the_hash_table.get(13))
        self.add_package(the_hash_table.get(14))
        self.add_package(the_hash_table.get(15))
        self.add_package(the_hash_table.get(16))
        self.add_package(the_hash_table.get(19))
        self.add_package(the_hash_table.get(20))
        self.add_package(the_hash_table.get(29))
        self.add_package(the_hash_table.get(30))
        self.add_package(the_hash_table.get(33))
        self.add_package(the_hash_table.get(34))
        self.add_package(the_hash_table.get(35))
        self.add_package(the_hash_table.get(37))
        self.add_package(the_hash_table.get(39))
        self.add_package(the_hash_table.get(40))

    # Manually loading truck #2 for its delivery route
    def load_truck_two(self, the_hash_table):
        self.add_package(the_hash_table.get(3))
        self.add_package(the_hash_table.get(6))
        self.add_package(the_hash_table.get(18))
        self.add_package(the_hash_table.get(25))
        self.add_package(the_hash_table.get(28))
        self.add_package(the_hash_table.get(31))
        self.add_package(the_hash_table.get(32))
        self.add_package(the_hash_table.get(36))
        self.add_package(the_hash_table.get(38))

    # Loading truck #3 for its delivery route
    def load_truck_three(self, the_hash_table):
        self.add_package(the_hash_table.get(2))
        self.add_package(the_hash_table.get(4))
        self.add_package(the_hash_table.get(5))
        self.add_package(the_hash_table.get(7))
        self.add_package(the_hash_table.get(8))
        self.add_package(the_hash_table.get(9))
        self.add_package(the_hash_table.get(10))
        self.add_package(the_hash_table.get(11))
        self.add_package(the_hash_table.get(12))
        self.add_package(the_hash_table.get(17))
        self.add_package(the_hash_table.get(21))
        self.add_package(the_hash_table.get(22))
        self.add_package(the_hash_table.get(23))
        self.add_package(the_hash_table.get(24))
        self.add_package(the_hash_table.get(26))
        self.add_package(the_hash_table.get(27))

    """
        start_route():
            Greedy/nearest neighbor algorithm. Locates next delivery using net_package_to_deliver() function.
            Then simulates delivery by updating trucks current_time, distance_traveled, current_location
            and manifest. Repeats this process till all packages have been "delivered"

        Args:
            self: the truck the function is be called on
            list_of_locations: the list of possible delivery locations and the distances between locations.
            It is primarily used to get distances between locations

        Returns:
            N/A

        Raises:
            N/A: This function raises no errors/has no error checking

        Time complexity:
            The time complexity of this function is O(N)

        Space complexity:
            The space complexity is also O(N)
    """
    def start_route(self, list_of_locations):
        # Once a truck starts its route all the packages on board have their delivery status set to "en route"
        for some_package in self.manifest:
            some_package.set_delivery_status("en route")
            some_package.set_time_package_left_hub(self.current_time)

        # Using while loop to iterate through a trucks manifest, until trucks manifest is empty
        # (all packages are delivered)
        while len(self.manifest) > 0:
            # Calling next_package_to_deliver() function to located delivery address closest to trucks current location
            package_being_delivered = self.next_package_to_deliver(list_of_locations)
            # Calculating distance between trucks current location and location of package_being_delivered
            # using distance_between_addresses() function
            distance_traveled = float(
                distance_between_addresses(self.current_location, package_being_delivered.get_address(),
                                           list_of_locations))
            # Adding distance traveled to truck's mileage
            self.add_distance(distance_traveled)
            # Calculation how long it took for truck to make delivery and updating truck's current time
            self.add_time(self.time_to_deliver(distance_traveled))
            # Updating packages delivery status delivered and adding time of delivery
            package_being_delivered.set_time_package_delivered(self.current_time)
            package_being_delivered.set_delivery_status("delivered at " + str(self.current_time))
            # Updating truck's current location to location of its list delivery
            self.set_current_location(package_being_delivered.get_address())
            # Removing delivered package from trucks manifest
            self.manifest.remove(package_being_delivered)

    # Directs delivery truck back to hub after it's completed its last delivery
    def return_to_hub(self, list_of_locations):
        distance_to_hub = float(
            distance_between_addresses(self.get_location(), '4001 South 700 East', list_of_locations))
        self.add_distance(distance_to_hub)
        self.add_time(self.time_to_deliver(distance_to_hub))
        self.set_current_location('4001 South 700 East')
