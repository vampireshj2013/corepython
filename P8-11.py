# -*- coding:utf-8 -*-
import string

l = []
i = 1
while True:
    name = raw_input("please enter name %d,enter [end] to end input:" % len(l))
    if name == 'end':
        break
    if not len(name.split(",")) == 2 and i < 4:
        print """Wrong format,shoule be Last,First
you have done this %d time(s),Fixing input""" % i
        i += 1
    else:
        l.append(name)
        i = 1

print l
