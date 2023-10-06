#!/usr/bin/python3
def no_c(my_string):
    my_newstring = ''
    for i in range(0, len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            my_newstring += ''
        else:
            my_newstring += my_string[i]
    return (my_newstring)


if __name__ == "__main":
    no_c()
