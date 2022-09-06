#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    new_dic.update((x, y * 2) for x, y in new_dic.items())
    return new_dic
