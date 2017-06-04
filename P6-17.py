# -*- coding:utf-8 -*-

def myPop(li):
    if not isinstance(li, list):
        raise TypeError, "input param must be list"
    if li:
        end = len(li)-1
        lastEle = li[end]
        li.remove(end)
        return lastEle
    else:
        raise TypeError, "list is empty"

li = [0,1,2,3]
print myPop(li)
print li
print myPop([])