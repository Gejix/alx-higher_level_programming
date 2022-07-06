#!/usr/bin/python3
""" Module 7-add_item
that adds all arguments to a Python list, and then
save them to a file
"""


import sys
import os.path


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_file('add_item.json')
except FileNotFoundError:
    my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_file(my_list, 'add_item.json')
