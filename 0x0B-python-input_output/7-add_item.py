#!/usr/bin/python3
""" Module 7-add_item
that adds all arguments to a Python list, and then
save them to a file
"""
import sys
import os


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists('add_item.json') is True:
    my_list = list(load_file("add_item.json"))
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_file(my_list, "add_item.json")
else:
    my_list = []
    save_file(my_list, "add_item.json")
