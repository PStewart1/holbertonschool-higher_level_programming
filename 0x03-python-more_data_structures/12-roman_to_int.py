#!/usr/bin/python3


def roman_to_int(roman):
    if (roman is None or type(roman) != str):
        return 0
    converter = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
    number = 0
    length = len(roman)
    i = 0
    while i < length:
        if i + 1 < length and roman[i:i + 2] in converter:
            number += converter[roman[i:i + 2]]
            i += 2
        else:
            number += converter[roman[i]]
            i += 1
    return number
