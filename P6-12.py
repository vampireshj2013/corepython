# -*- coding:utf-8 -*-
def findchar(string, char):
    if not isinstance(char, str):
        raise ValueError("input param is not valid.")
    if len(char) != 1:
        raise ValueError, "input param is not char"
    if not string:
        return -1

    for i in range(len(string)):
        if string[i] == char:
            return i
    return -1


def rfindchar(string, char):
    if not isinstance(char, str):
        raise ValueError("input param is not valid.")
    if len(char) != 1:
        raise ValueError, "input param is not char"
    if not string:
        return -1

    for i in range(len(string) - 1, -1, -1):
        if string[i] == char:
            return i
    return -1


def subchar(string, char, newchar):
    if not isinstance(char, str):
        raise ValueError("input param is not valid.")
    if len(char) != 1:
        raise ValueError, "input param is not char"
    if not string:
        return -1
    new_char = ''
    for i in range(len(string)):
        if string[i] == char:
            new_char += newchar
        else:
            new_char += string[i]
    return new_char


print findchar("123436", '3')
print rfindchar("123436", '3')
print subchar("123436", '3', 'S')
