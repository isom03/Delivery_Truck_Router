# Class builds adjacency list to store distances between locations
import csv

"""
    index_of_address:
        Function locates the index of a specific address within a given list of locations and returns the index

    Args:
        address: is the address being looked for and is represented as a string
        locations: a list of all locations WGUPS will be delivering to

    Returns:
        the index of an address in the list as an integer

    Raises:
        N/A: This function raises no errors/has no error checking

    Time complexity:
        The time complexity of this function is O(N)

    Space complexity:
        The space complexity is also O(N)
"""


def index_of_address(address, locations):
    index = 0
    while True:
        the_address = locations[index][0]
        if address in the_address:
            return index
        else:
            index += 1


"""
    distance_between_addresses:
        Function calculates the distance between two addresses, given the addresses and an adjacency list which stores
        the distance between any address you'll have to deliver to 

    Args:
        address_1: is the first address being looked up and is represented as a string
        address_2: is the second address being looked up and is represented as a string
        locations: a list of all locations WGUPS will be delivering to

    Returns:
        the distance between address_1 and address_2 as an integer

    Raises:
        N/A: This function raises no errors/has no error checking

    Time complexity:
        The time complexity of this function is O(N)

    Space complexity:
        The space complexity is also O(N)
"""


def distance_between_addresses(address_1, address_2, locations):
    # Locating index of address_1 in adjacency list
    index_of_address_1 = index_of_address(address_1, locations)
    # Locating index of address_2 in adjacency list which is off by 1 do to formatting of list
    index_of_address_2 = index_of_address(address_2, locations) + 1
    # Returning distance between locations
    return locations[index_of_address_1][index_of_address_2]


"""
    get_locations_from_file:
        Creating my own adjacency list to store addresses read from WGUPS distance file

    Args:
        file_name: name of CSV file to be opened, represented as string
        adjacency_list: list to store rows from 
    
    Returns:
        N/A

    Raises:
        N/A: This function raises no errors/has no error checking

    Time complexity:
        The time complexity of this function is O(N)

    Space complexity:
        The space complexity is also O(N)
"""


def get_locations_from_file(file_name, adjacency_list):
    with open(file_name, 'r') as WGUPS_Location_File:
        list_of_locations = csv.reader(WGUPS_Location_File)
        next(list_of_locations)
        for row in list_of_locations:
            adjacency_list.append(row)
