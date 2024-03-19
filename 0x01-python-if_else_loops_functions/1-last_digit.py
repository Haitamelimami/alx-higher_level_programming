#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    l_dgt = number % 10
else:
    l_dgt = number % -10

print("Last digit of {:d} is {:d}".format(number, l_dgt))

if l_dgt > 5:
    print(" and is greater than 5")
elif l_dgt == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
