# -*- coding:utf-8 -*-
a = "   abcd  "
print "start" + a + "end"
print "start" + a.lstrip() + "end"
print "start" + a.rstrip() + "end"
print "start" + a.strip() + "end"


def mystrip(a):
    """

    :param a: string that has to be process
    :return: new string that head,tail blank has deleted
    """
    if a:
        start=0
        end = 0
        for i in range(len(a)):
            if a[i] != ' ':
                start = i
                break
        for i in range(len(a)-1,0,-1):
            if a[i] != ' ':
                end = i
                break
        if start == end == 0:
            return a
        else:
            return a[start:end]
    else:
        return a
print mystrip(a)

