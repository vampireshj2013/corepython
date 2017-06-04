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
correct = False
for i in range(3):
    M_input = raw_input("please input A|B,element split with  \",\":\n")
    M = set([int(x) for x in M_input.split(",")])
    if M == A | B:
        print "Correct!"
        correct = True
        break
    else:
        print "Wrong!"
else:
    print "True Answer of A|B:%s\n" % str(A | B)
