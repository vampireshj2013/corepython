# -*-coding:utf-8-*-

a = {"username": "wanghaijiang"}
b = {"age": "18"}
a.update(b)
print a
sort_keys = a.keys()
sort_keys.sort()
for s in sort_keys:
    print s, a[s]
