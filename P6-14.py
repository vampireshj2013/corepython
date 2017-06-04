# -*- coding:utf-8 -*-
import random

r = [['E', 'L', 'W'], ['W', 'E', 'L'], ['L', 'W', 'E']]
dict1 = {'E': "平手", 'L': "你输了", 'W': '你赢了'}
s = ['石头', '剪刀', '布']
a = int(raw_input("请选择出0：石头，1：剪刀，2：布\n"))
print "你出的是：%s" % s[a]
b = random.randint(0, 2)
print "电脑出的是：%s" % s[b]

print dict1.get(r[b][a])
