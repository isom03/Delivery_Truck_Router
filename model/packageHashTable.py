# Hash Map
class PackageHashTable:
    # constructor for class
    def __init__(self):
        # size will be size or length of array
        self.size = 10
        # map is the name of the array or list. Each value is set to None
        self.table = [None] * self.size

    # Actual function which computes index where object will be stored in array
    # Time complexity of O(1)
    def _get_hash(self, key):
        hash = key % 10
        return hash

    """
        add:
            Function adds a key value pair to hash table

        Args:
            key: an integer used to represent key or index in hash table
            value: will be a package object

        Returns:
            boolean value of True once completed

        Raises:
            N/A: This function raises no errors/has no error checking

        Time complexity:
            The time complexity of this function is O(N)

        Space complexity:
            The space complexity is also O(N)
    """

    # function adds a key value pair to hashmap
    # Time complexity of O(N)
    def add(self, key, value):
        # key_hash stored result of _get_hash function
        # more specifically the index position in which the object will be stored in array
        key_hash = self._get_hash(key)

        # key_value is simply the combination of the key and value which will be stored in the array
        key_value = [key, value]

        # Checking to sey if array/list is empty at calculated index.
        # If it is empty the index will be set to the key_value
        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        # Else go to index of list and begin iterating through to see if key is already listed
        else:
            for pair in self.table[key_hash]:
                # If key is already listed its associated pair will be updated
                if pair[0] == key:
                    pair[1] == value
                    return True
            # If a matching key cannot be found in the index it will be added to list at index
            self.table[key_hash].append(key_value)
            return True

    """
        get:
            Function returns a value stored at a given key.

        Args:
            key: an integer used to represent key or index in hash table

        Returns:
            the package stored at the given key or None if no package is stored there

        Raises:
            N/A: This function raises no errors/has no error checking

        Time complexity:
            The time complexity of this function is O(N)

        Space complexity:
            The space complexity is also O(N)
    """

    def get(self, key):
        # getting index of value using key and _get_hash function
        key_hash = self._get_hash(key)
        # if there are values stored at index function will iterate through pairs stored at index
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        # else will function will return none or null showing no value is stored at key
        return None
