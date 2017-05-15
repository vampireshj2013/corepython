# -*-coding:utf-8-*-
import math


def getfactors(num):
    """
    
    :param num: 
    :return: factors set of num 
    """
    s = set()
    for i in range(1, num):
        if num % i == 0:
            s.add(i)
    return s


print sorted(getfactors(20))
print sorted(getfactors(24))
