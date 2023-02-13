#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    my_l_3 = []
    for i in range(0, list_length):
        try:
            my_l = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            my_l = 0
        except ZeroDivisionError:
            print("division by 0")
            my_l = 0
        except IndexError:
            print("out of range")
            my_l = 0
        finally:
            my_l_3.append(my_l)
    return (my_l_3)
