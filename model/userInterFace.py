from datetime import timedelta


"""
    get_all_package_info:
        Function iterates through a hash table and prints off all package information

    Args:
        the_hash_table: the hash table storing all package information
        truck_one_distance: is float and is the distance traveled by delivery truck #1
        truck_two_distance: is a float and is the distance traveled by delivery truck #2
        truck_three_distance: is a float and is the distance traveled by delivery truck #3

    Returns:
        N/A

    Raises:
        N/A: This function raises no errors/has no error checking

    Time complexity:
        The time complexity of this function is O(N)

    Space complexity:
        The space complexity is also O(N)
"""


def get_all_package_info(the_hash_table, truck_one_distance, truck_two_distance, truck_three_distance):
    total_mileage = truck_one_distance + truck_two_distance + truck_three_distance
    print("The total distance traveled by the three delivery trucks was " + str(total_mileage) + " miles")
    print("Status of All Packages: ")
    index = 1
    while index <= 40:
        temp_package = the_hash_table.get(index)
        temp_package.print_package_info()
        index += 1
    return None


"""
    status_of_package_given_time:
        Function returns the status of a package upon a user entering a package ID # and specific time.

    Args:
        the_hash_table: the hash table storing all package information

    Returns:
        N/A

    Raises:
        N/A: This function raises no errors/has no error checking

    Time complexity:
        The time complexity of this function is O(N)

    Space complexity:
        The space complexity is also O(N)
"""


def status_of_package_given_time(the_hash_table):
    package_id = int(input("Please enter a package ID number: "))
    user_package = the_hash_table.get(package_id)
    print("Please enter enter the time you want to look at in hours and minutes.")
    hours = int(input("Hour(s): "))
    minutes = int(input("Minute(s): "))
    user_time = timedelta(hours=hours, minutes=minutes)
    if user_package.get_time_package_delivered() <= user_time:
        user_package.print_package_info()
    elif user_package.get_time_package_left_hub() >= user_time:
        user_package.alt_print_package_info(user_time, " it is still at hub")
    else:
        user_package.alt_print_package_info(user_time, " its out for delivery")
    return None


"""
    status_of_all_packages_given_time:
        Function returns the status of each package given a specific time entered by user

    Args:
        the_hash_table: the hash table storing all package information

    Returns:
        N/A

    Raises:
        N/A: This function raises no errors/has no error checking

    Time complexity:
        The time complexity of this function is O(N)

    Space complexity:
        The space complexity is also O(N)
"""


def status_of_all_packages_given_time(the_hash_table):
    print("Please enter enter the time you want to look at in hours and minutes.")
    hours = int(input("Hour(s): "))
    minutes = int(input("Minute(s): "))
    user_time = timedelta(hours=hours, minutes=minutes)
    print("Status of All Packages: ")
    index = 1
    while index <= 40:
        temp_package = the_hash_table.get(index)
        if temp_package.get_time_package_delivered() <= user_time:
            temp_package.print_package_info()
        elif temp_package.get_time_package_left_hub() >= user_time:
            temp_package.alt_print_package_info(user_time, " it is still at hub")
        else:
            temp_package.alt_print_package_info(user_time, " its out for delivery")
        index += 1
    return None
