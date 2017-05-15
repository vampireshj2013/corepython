# -*-coding:utf-8-*-
import math


def isperfect(num):
    """
    
    :param num: 
    :return: factors set of num 
    """
    s = set()
    for l in range(1, num):
        if num % l == 0:
            s.add(l)
    return math.fsum(s) == num


for i in range(10000000):
    if isperfect(i):
        print i, "\t",
