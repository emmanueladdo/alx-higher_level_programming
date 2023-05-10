#!/usr/bin/python3
numb = 0
while numb <= 89:
    if numb % 10 == 0:
        numb += 1 + numb // 10
    print("{:02d}".format(numb), end='\n' if numb == 89 else ", ")
    numb += 1
