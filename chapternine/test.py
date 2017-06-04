# -*- coding:utf-8 -8-
import os

f = open("t.txt", "r+")
print f.read()
f.seek(0)
print f.readline()
f.seek(0)
for line in f.readlines():
    print line,

f.seek(0)

print "---"
for line in f:
    print line

print "text():", f.tell()
f.seek(0)
print f.next()
f.seek(0)
print f.truncate(11)
f.close()

print os.linesep, os.sep, os.pathsep, os.curdir, os.pardir
