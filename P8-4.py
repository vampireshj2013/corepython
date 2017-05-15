# -*-coding:utf-8-*-
import math


def isprime(num):
    """
    
    :param num: 
    :return: judge num is prime
    """
    r = int(math.sqrt(num)) + 1
    for i in range(2, r):
        if num % i == 0:
            return False
    return True


print isprime(4)
print isprime(5)
print isprime(6)
print isprime(7)
