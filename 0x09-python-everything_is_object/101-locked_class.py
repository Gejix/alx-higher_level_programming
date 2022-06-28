#!/usr/bin/python3
"""
Module 101-locked_classes
This is a module that containts a class that avoids
dynmaically created attributes
"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
