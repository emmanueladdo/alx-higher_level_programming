#!/usr/bin/python3
def complex_delete(my_dict, value):
    dulp = my_dict.copy()
    for key, value in dulp.items():
        if item in value:
            del my_dict[key]
    return my_dict
