#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ltdi = number % 10 if number > 0 else int(repr(number)[-1]) * -1
if (ltdi > 5):
    print(f"Last digit of {number:d} is {ltdi:d} and is greater than 5")
elif (ltdi == 0):
    print(f"Last digit of {number:d} is {ltdi:d} and is 0")
else:
    print(f"Last digit of {number:d} is {ltdi:d} and is less than 6 and not 0")
