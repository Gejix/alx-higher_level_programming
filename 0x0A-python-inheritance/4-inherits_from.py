#!/usr/bin/python3
"""
Module 4-inherits_from
Function that returns True/False if obj is a type of a_class
"""


def inherits_from(obj, a_class):
    """Args:
        obj: object
        a_class: class type
    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    if issubclass(type(obj), a_class) and (type(obj) != a_class):
        return True
    return False
