# -*- coding:utf-8 -*-

a = 1 + 2j


def atoc(string):
    if not string:
        raise TypeError, "input param is empty"
    if not isinstance(string, str):
        raise TypeError, "input param type is Error."
    if string.find('j') > 0 or string.find('J') > 0:
        index = 0
        for i in range(len(string) - 1, -1, -1):
            if string[i] in ['+', '-']:
                index = i
        if index == 0:
            real = 0
        else:
            real = float(string[:index])
        image = float(string[index:len(string) - 1])
        return complex(real, image)
    else:
        return complex(float(string))


print atoc("-2j")
