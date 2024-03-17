#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tem = my_list[:]
    if idx < 0 or idx > len(my_list) - 1:
        return tem
    tem[idx] = element
    return tem
