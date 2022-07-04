#!/usr/bin/python3
"""
Module 1-my_list
Function that returns the list of available attributes
and methods of an object
"""


class MyList(list):
    """ Class that inherits the attributes references of class list
    Args:
        list: class list
    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
