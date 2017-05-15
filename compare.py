# -*-coding:utf-8-*-
L = [{1: 5, 3: 4}, {1: 3, 6: 3}, {1: 1, 2: 4, 5: 6}, {1: 9}]


def f(x):
    return len(x)


L.sort(key=f)
print L
print sorted(L, key=f)
