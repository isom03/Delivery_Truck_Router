# Isom Brown
# Student ID: 004478495
# The write-up for this project is located in the c950Data folder with the CSV files used.

# Importing created classes
from datetime import timedelta
from model.packageHashTable import PackageHashTable
from model.package import Package
from model.truck import DeliveryTruck
from model.locationDistances import get_locations_from_file
from model.userInterFace import get_all_package_info, status_of_package_given_time, status_of_all_packages_given_time

# Creating list to store location and distance information
list_of_locations = []

# Creating a hash map from own hash map class
the_hash_table = PackageHashTable()

# Using get_packages_file() to read package from CSV file into the_hash_map
Package.get_packages_from_file('c950Data/WGUPS_Package_File.csv', the_hash_table)

# Using get_locations_from_file() to read location and distance data from CSV file into list_of_locations
get_locations_from_file('c950Data/The_WGUPS_Distance_Table.csv', list_of_locations)

# Creating my three delivery trucks used to deliver packages. All are empty initially
truck_one = DeliveryTruck()
truck_two = DeliveryTruck()
truck_three = DeliveryTruck()

# Loading trucks
truck_one.load_truck_one(the_hash_table)
truck_two.load_truck_two(the_hash_table)
truck_three.load_truck_three(the_hash_table)

# Truck one starts its delivery route
truck_one.start_route(list_of_locations)

# Truck two will start its route once the delayed packages arrive at the hub
truck_two.set_time(timedelta(hours=9, minutes=5))
truck_two.start_route(list_of_locations)

# Truck three will start its route once truck #1 has returned and delivery address for package #9 is updated
truck_three.set_time(timedelta(hours=10, minutes=20))
misaddressed_package = the_hash_table.get(9)
misaddressed_package.set_address("410 S State St")
misaddressed_package.set_zip("84111")
truck_three.start_route(list_of_locations)

# Boolean run_program allows while loop to keep executing until user is done with program
run_program = True

# While prints out a Menu for user to interact with delivery program. User can exit program anytime they decide
while run_program:
    print("Menu Options:\n"
          "***************************************\n"
          "1. Print the Status of All Packages and Total Mileage at End of Day\n"
          "2. Get Status of Specific Package at Specific Time\n"
          "3. Get Status of All Packages at Specific Time\n"
          "4. Exit the Program\n"
          "***************************************")
    val = int(input("Choose an option (1, 2, 3 or 4):  "))
    print("\n")
    # Printing the status of all packages and total mileage using get_all_package_info(), if user selects "1"
    if val == 1:
        get_all_package_info(the_hash_table, truck_one.get_distance_traveled(), truck_two.get_distance_traveled(),
                             truck_three.get_distance_traveled())
        print("\n")
    # Printing the status of specific package at a specific time using status_of_package_given_time()
    #  if user selects "2"
    elif val == 2:
        status_of_package_given_time(the_hash_table)
        print("\n")
    # Print the status of all packages given a specific time using status_of_all_packages_given_time()
    # if user selects "3"
    elif val == 3:
        status_of_all_packages_given_time(the_hash_table)
        print("\n")
    # If user selects "4", run_program is set to false and the while loop keeping the program running will terminate
    elif val == 4:
        run_program = False
    else:
        print("Please enter a valid input\n\n")
