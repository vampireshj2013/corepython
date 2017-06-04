# -*- coding:utf-8 -*-

print range(0, 102, 3)
input = raw_input("请输入1:按行输出,0:按列输出\n")
rawNum = raw_input("行数：\n")
li = [i for i in range(100)]
raw = int(input)
rawNum = int(rawNum)
size = len(li)
if raw:
    # 按行输出
    num = size / rawNum
    for i in range(0, size, num):
        end = i + num
        if size - end < rawNum:
            end = size
        print li[i:end]
        if end == size:
            break

else:
    # 按列输出
    if size % rawNum:
        a = (size / rawNum + 1) * rawNum - size
        for i in range(a):
            li.insert(len(li) - 1, " ")

    for i in range(0, size, rawNum):
        print li[i:i + rawNum]
