#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
        "I": 1, "V": 5,
        "X": 10, "L": 50,
        "C": 100, "D": 500,
        "M": 1000}
    if roman_string is None or type(roman_string) is not str:
        return 0
    n = len(roman_string)
    value = roman[roman_string[n - 1]]
    for i in range(n - 1, 0, -1):
        current_v = roman[roman_string[i]]
        previous_v = roman[roman_string[i - 1]]

        if previous_v >= current_v:
            value += previous_v
        else:
            value -= previous_v
    return value
