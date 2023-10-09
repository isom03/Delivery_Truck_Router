# Class for packages
from model.packageHashTable import PackageHashTable
import csv


class Package:
    # Constructor for package object.
    def __init__(self, package_id, address, city, state, zipcode, delivery_deadline, package_weight, special_notes,
                 delivery_status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self.package_weight = package_weight
        self.special_notes = special_notes
        self.delivery_status = delivery_status
        self.time_package_left_hub = None
        self.time_package_delivered = None

    # Creating getters and setters for package variables/fields
    def get_id(self):
        return self.package_id

    def set_id(self, id_num):
        self.package_id = id_num

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_zip(self):
        return self.zipcode

    def set_zip(self, zip):
        self.zipcode = zip

    def get_delivery_deadline(self):
        return self.delivery_deadline

    def set_delivery_deadline(self, deadline):
        self.delivery_deadline = deadline

    def get_package_weight(self):
        return self.package_weight

    def set_package_weight(self, weight):
        self.package_weight = weight

    def get_special_notes(self):
        return self.special_notes

    def set_special_notes(self, note):
        self.special_notes = note

    def get_delivery_status(self):
        return self.delivery_status

    def set_delivery_status(self, status):
        self.delivery_status = status

    def set_time_package_left_hub(self, departure_time):
        self.time_package_left_hub = departure_time

    def get_time_package_left_hub(self):
        return self.time_package_left_hub

    def set_time_package_delivered(self, arrival_time):
        self.time_package_delivered = arrival_time

    def get_time_package_delivered(self):
        return self.time_package_delivered

    """
        get_packages_from_file:
            Function takes a file name and hashmap. It then takes information from file to create package objects which
            are placed in the hash table

        Args:
            file_name: name of CSV file to be opened, represented as string
            the_table: hash table used to store packages.

        Returns:
            N/A

        Raises:
            N/A: This function raises no errors/has no error checking

        Time complexity:
            The time complexity of this function is O(N)

        Space complexity:
            The space complexity is also O(N)
    """

    def get_packages_from_file(file_name, the_table):
        with open(file_name, 'r') as WGUPS_Package_File:
            # Placing lines from file in list I can iterate through
            package_list = csv.reader(WGUPS_Package_File)
            # Getting through lines of file without package info
            next(package_list)
            next(package_list)
            # Iterating through a row (or line) from the file and storing information in variables that will be used
            # to create package object shortly
            for row in package_list:
                package_id = int(row[0])
                address = row[1]
                city = row[2]
                state = row[3]
                zipcode = row[4]
                delivery_deadline = row[5]
                package_weight = row[6]
                special_notes = row[7]
                delivery_status = "at hub"

                # Creating instance of package
                package = Package(package_id, address, city, state, zipcode, delivery_deadline, package_weight,
                                  special_notes, delivery_status)

                # Passing package_id and actual package into hash map
                the_table.add(package_id, package)

    # Function allows me to print off all info associated with a package.
    def print_package_info(self):
        print("Package #" + str(self.package_id) + ": was delivered to", self.get_address(), self.get_city(),
              self.get_state(), self.get_zip(), "the delivery deadline was", self.get_delivery_deadline(),
              "the package weighed", self.get_package_weight(), "kilos. The package was delivered at",
              self.time_package_delivered)

    # Function allows me to print off all info associated with a package. Substituting in a user's selected time and
    # the status of the package at that particular time.
    def alt_print_package_info(self, user_time, status_at_user_time):
        print("Package #" + str(self.package_id) + ": is set to be delivered to", self.get_address(), self.get_city(),
              self.get_state(), self.get_zip(), "the delivery deadline is", self.get_delivery_deadline(),
              "the package weighed", self.get_package_weight(), "kilos. At " + str(user_time) +
              status_at_user_time)
