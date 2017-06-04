# -*- coding:utf-8 -*-
input_str = raw_input("Enter a number string:\n")
a = ""
for i in input_str:
    if i.isupper():
        a += i.lower()
    elif i.islower():
        a += i.upper()
    else:
        a += i
print a

