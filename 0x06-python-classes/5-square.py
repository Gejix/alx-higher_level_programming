#!/usr/bin/python3
"""
M0dule 5-square
Define class Square
"""


class Square:
    """ Defines a Class square object.
    Private instance attribute: size.
    """

    def __init__(self, size=0):
        """ initialize the method square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method that returns the square are of the object
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Method that returns to the current
        the square area of the object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ A Method that prints a number of # squares
        according to the size value given
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
