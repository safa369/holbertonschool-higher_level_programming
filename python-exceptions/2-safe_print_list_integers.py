#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_p = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            nb_p += 1
        except (ValueError, TypeError):
            continue
    print("")
    return nb_p