# -*-coding:utf-8-*-
import random


def genSet():
    A = set()
    N = random.randint(0, 10)
    for i in range(0, N + 1):
        A.add(random.randint(0, 9))
    return A


A = genSet()
B = genSet()

print "A:", A
print "B:", B
print "A|B:", A | B
print "A&B:", A & B


