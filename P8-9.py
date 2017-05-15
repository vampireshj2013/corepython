# -*- coding:utf-8 -*-
import math


def fibonacci(N):
    """
    
    :param num: 
    :return: N!
    """
    if N <= 2:
        return 1
    else:
        return fibonacci(N - 1) + fibonacci(N - 2)


print fibonacci(6)
