#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    if my_list is None:
        return
    for i in range(0, len(my_list)):
        print('{:d}'.format(my_list[i]), end='\n')


if __name__ == "__main__":
    print_reversed_list_integer()
