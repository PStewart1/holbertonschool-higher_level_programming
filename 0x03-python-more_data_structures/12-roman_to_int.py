#!/usr/bin/python3


def roman_to_int(roman_string):
    number = 0
    for i in range(len(roman_string)):
        if roman_string[i] == "I":
            if (roman_string[i - 1] == "I" or
                (roman_string[i + 1] != "V" and
                    roman_string[i + 1] != "X")):
                        number += 1
            elif roman_string[i + 1] == "V":
                number += 4
            elif roman_string[i + 1] == "X":
                number += 9
        if roman_string[i] == "V":
            if roman_string[i - 1] == "I":
                continue
            else:
                number += 5
        if roman_string[i] == "X":
            if roman_string[i - 1] == "I":
                continue
            if (roman_string[i - 1] == "X" or
                (roman_string[i + 1] != "L" and
                    roman_string[i + 1] != "C")):
                        number += 10
            elif roman_string[i + 1] == "L":
                number += 40
            elif roman_string[i + 1] == "C":
                number += 90
        if roman_string[i] == "L":
            if roman_string[i - 1] == "X":
                continue
            else:
                number += 50
        if roman_string[i] == "C":
            if roman_string[i - 1] == "X":
                continue
            if (roman_string[i - 1] == "C" or
                (roman_string[i + 1] != "D" and
                    roman_string[i + 1] != "M")):
                        number += 100
            elif roman_string[i + 1] == "D":
                number += 400
            elif roman_string[i + 1] == "M":
                number += 900
        if roman_string[i] == "D":
            if roman_string[i - 1] == "C":
                continue
            else:
                number += 500
        if roman_string[i] == "M":
            if roman_string[i - 1] == "C":
                continue
            if roman_string[i - 1] == "M":
                number += 1000
    return number
