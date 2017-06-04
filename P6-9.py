# -*- coding:utf-8 -*-
import string

number_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num_str = raw_input("Enter a number string:\n")
value = ""
if num_str.isdigit():
    for i in num_str:
        value += number_list[int(i)] +  "-"
    print value[0:len(value)-1]
else:
    print "input number is not valid."
