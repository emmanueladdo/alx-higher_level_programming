#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for item in range(x):
            if isinstance(my_list[item], int):
                count += 1
                print("{:d}".format(my_list[item]), end="")
    except TypeError as err:
        print(err)
    else:
        print("")
        return count
