#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= len(my_list) or idx < 0:
        return(my_list)
    else:
        lst = my_list.copy()
        lst[idx] = element
        return(lst)


if __name__ == "__main__":
    new_in_list()
