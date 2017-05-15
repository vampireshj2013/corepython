# -*- coding:utf-8 -*-
import math


def factors(N):
    """
    
    :param num: 
    :return: N!
    """
    if N == 1:
        return N
    else:
        return N * factors(N - 1)


print factors(20)
