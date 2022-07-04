#!/usr/bin/python3
"""
Module 0-lookup
Function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    Args:
        obj: instance of the class
    Returns:
        List of attributes
    """

    return dir(obj)
