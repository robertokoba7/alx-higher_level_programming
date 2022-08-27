#!/usr/bin/python3
def element_at(my_list, idx):
    if idx == "-":
        return (None)
    elif idx > my_list:
        return (None)
    else:
        print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
