#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) is 0:
        return 0
    i = list(map(list, zip(*my_list)))
    w = [x * y for x, y in zip(i[0], w[1])]
    return sum(i) / sum(w[1])
