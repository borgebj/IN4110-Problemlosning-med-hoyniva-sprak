import random
import statistics

"""
Array class for assignment 2
"""


def validShape(shape):
    """Checks if tuple defining shape is of right type
    param:
        shape (tuple): Tuple that decides type of array
    return:
        bool: True if shape is tuple, else false
    """
    return isinstance(shape, tuple)


def validTypes(other):
    """Checks if tuple of values has valid datatypes for array
    param:
        other (tuple): Tuple of values
    return:
        bool: True if tuple is valid , else false
    """
    return len([value for value in other if not isinstance(value, (int, float, bool))]) == 0


def homogenous(other):
    """Checks if tuple of values is homogeneous

    Creates a list of all types in the tuple.
    Turns it into a set so only one of each type is added
    Checks if length of set  is only 1, as in only 1 datatype

    param:
        other (tuple): Tuple of values
    return:
        bool: True if tuple only has one datatype, else false
    """
    return len(set([type(x) for x in other])) == 1


def supportSize(other, shape):
    """Checks type of array, then checks if amount of values in array is equal to or less than the max size
       Only supports _2_ dimensions currently

    param:
        other (tuple): tuple of elements
        shape (tuple): Tuple that decides type of array
    return:
        bool: True if array supports given size, else false
    """
    if len(shape) == 2:
        return len(other) == shape[0] * shape[1]
    return len(other) == shape[0]


class Array:

    def __init__(self, shape, *values):
        """Initializing array of 1-dimensionality with only types:
        - int / float /bool

        Checks for both type-correctness and same-value check to ensure array is homogeneous
        Creates either a 1D-array or 2D-array based on shape

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. Can only be either int, float or boolean.
        """
        # Sets instance attributes
        self.shape = shape
        self.arr = []
        self.type = type(random.choice(values))

        # checks the values and fills array according to shape
        self.checkInput(values)
        self.arr = self.fillArr(list(values))

        # uses the inserted list to operate on
        self.flat = values

    # -- call helping functions --

    def checkInput(self, values):
        """Takes in a tuple of values and performs various checks
        param:
            values (tuple): tuple of values
        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        # Checks if tuple is homogenous
        if not homogenous(values):
            raise ValueError("Values given are not homogenous")

        # check if shape is of valid type
        if not validShape(self.shape):
            raise TypeError("Shape is of wrong type")

        # Checks if value size is same as shape dictates
        if not supportSize(values, self.shape):
            raise ValueError("Invalid size of shape and values")

        # checks if tuple includes only valid types
        if not validTypes(values):
            raise TypeError("Values are of wrong type")

    def fillArr(self, values):
        """Fills the array with given values according to shape

        note: example used in assignment 2 when indexing would be result if
              values.pop() were used instead of values.pop(0).
              I decided to pop from start to end instead.
        param:
            values (list):
        return:
            list: either a 1d or 2d list
        """
        if len(self.shape) == 1:
            return values
        elif len(self.shape) == 2:
            return [[values.pop(0) for _ in range(self.shape[0])] for _ in range(self.shape[1])]

    # -- -- -- -- -- -- -- --

    def __getitem__(self, item):
        """Returns element at given index position
        param:
            item (int): int representing index
        return:
            int/bool/float: element at given index
        """
        return self.arr[item]

    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        return str([x for x in self.arr])

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        Returns NotImplemented or raises exception if operation is not supported

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        if not isinstance(other, (Array, float, int)):
            return NotImplemented

        if isinstance(other, (int, float)):
            return Array(self.shape, *[value + other for value in self.flat])
        else:
            if self.shape.__eq__(other.shape):
                return Array(self.shape, *[i + j for i, j in zip(self.flat, other.flat)])
            raise ValueError("Invalid size on arrays")

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        Calls __add__ so it works on both ends

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        Returns NotImplemented or raises exception if operation is not supported

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        if not isinstance(other, (Array, float, int)):
            return NotImplemented

        if isinstance(other, (int, float)):
            return Array(self.shape, *[value - other for value in self.flat])
        else:
            if self.shape.__eq__(other.shape):
                return Array(self.shape, *[i - j for i, j in zip(self.flat, other.flat)])
            raise ValueError("Invalid size on arrays")

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        Calls __sub__ so it works on both ends

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        return self.__sub__(other)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        Returns NotImplemented or raises exception if operation is not supported

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        if not isinstance(other, (Array, float, int)):
            return NotImplemented

        if isinstance(other, (int, float)):
            return Array(self.shape, *[value * other for value in self.flat])
        else:
            if self.shape.__eq__(other.shape):
                return Array(self.shape, *[i * j for i, j in zip(self.flat, other.flat)])
            raise ValueError("Invalid size on arrays")

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        Calls __mul__ so it works on both ends

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        Checks if both shape and values is equal

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        return other.arr.__eq__(self.arr) and other.shape.__eq__(self.shape)

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        Raises error if the two array shapes do not match size
        Returns TypeError if value-types of array is invalid

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """
        if not isinstance(other, (Array, float, int)):
            return TypeError("Invalid operation on value-type")

        if isinstance(other, (int, float)):
            return Array(self.shape, *[x == other for x in self.flat])
        else:
            if self.shape.__eq__(other.shape):
                return Array(self.shape, *[i == j for i, j in zip(self.flat, other.flat)])
            raise ValueError("Invalid size on arrays")

    def min_element(self):
        """Returns the smallest value of the array.

        Only work for type int and float

        Returns:
            float: The value of the smallest element in the array.

        """
        if self.type in (float, int):
            return float(min(self.flat))
        raise TypeError("Invalid operation on value-type")

    def mean_element(self):
        """Returns the mean value of an array

        Only works for int and float

        Returns:
            float: the mean value
        """
        if self.type in (float, int):
            return float(statistics.mean(self.flat))
        raise TypeError("Invalid operation on value-type")
