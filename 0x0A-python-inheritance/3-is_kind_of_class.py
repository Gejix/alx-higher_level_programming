#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Function that returns True/False if obj is a type of a_class
"""


def is_kind_of_class(obj, a_class):
    """Args:
        obj: object
        a_class: class type
    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
