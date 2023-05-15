#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        """perfom checks"""
        max_n = my_list[0]
        for num in my_list:
            if num > max_n:
                max_n = num

        return (max_n)
