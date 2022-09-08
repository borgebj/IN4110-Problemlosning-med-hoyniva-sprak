import random

"""
Array class for assignment 2
"""


class Array:

    def __init__(self, shape, *values):
        """Initialize an array of 1-dimensionality. Elements can only be of type:

        - int
        - float
        - bool

        Make sure the values and shape are of the correct type.

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either int, float or boolean.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """

        # Sets instance attributes
        self.shape = shape
        self.values = []
        self.type = type(random.choice(values))

        # Checks if the values are of valid types
        if not self.validType(values):
            raise ValueError
        # assert len(([x for x in values if not isinstance(x, (float, int, bool))])) == 0

        # Checks that the amount of values corresponds to the shape
        assert len([x for x in values if not isinstance(x, type(shape[0]))]) == 0

        # Checks if value size is same as shape dictates
        if not self.supportSize(values):
            raise ValueError
        # assert len(values) <= (shape[0])

        # creates the array
        for value in values:
            self.values.append(value)

    def validType(self, other):
        return len([value for value in other if not isinstance(value, (int, float, bool))]) == 0

    def supportSize(self, other):
        return len(other) <= self.shape[0]

    def __getitem__(self, item):
        return self[item]

    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        pass

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        # Array + number = increment every number in list with number
        # Array + Array = check if size supports, then add
        # else NotImplemented
        if isinstance(other, (Array, float, int)):
            if isinstance(other, Array):

            else:
                return [value + other for value in self.values] # feil??
        else:
            return NotImplemented


        # check that the method supports the given arguments (check for data type and shape of array)
        # if the array is a boolean you should return NotImplemented

        pass

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        pass

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        # array - number = decrease every number
        # array - array = decrease every number by index
        if isinstance(other, (Array, float, int)):
            if isinstance(other, Array):
                if self.shape.__eq__(other.shape): # sjekk om like store
                    for i in range(0, len(self.values)):
                        self.values[i] -= other.values[i]
                    return self.values
                else: raise Exception(ValueError)
                # minus hver index med hverandre
            else:
                return [value - other for value in self.values]
        else:
            return NotImplemented


    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        pass

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # array * array = multily each index
        if isinstance(other, (Array, float, int)):
            if isinstance(other, Array):
                if self.shape.__eq__(other.shape): # sjekk om like store
                    for i in range(0, len(self.values)):
                        self.values[i] *= other.values[i]
                    return self.values
                else: raise ValueError
                    #return [self.values[x] * other[x] for x in range(0, len(self.values))]
            else:
                return [value * other for value in self.values]
        else:
            return NotImplemented

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """

        if self.validType(other):
            return self.values.__eq__(other.values)
        return False

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """

        pass

    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """

        pass

    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """

        pass


def run():
    a = Array((4,), 1, 2, 3)
    b = Array((3,), 5, 6)
    c = Array((3,), 1, 5)
    d = 5

    print(b * c)




run()
