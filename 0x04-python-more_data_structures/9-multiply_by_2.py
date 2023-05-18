#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for key, value in my_dict.items():
        new_dict[key] = value * 2
    return new_dict
