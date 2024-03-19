#!/usr/bin/python3
for car in range(97, 123):
    if car != 101 and car != 113:
        print("{:c}".format(car), end='')
