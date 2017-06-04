# -*-coding:utf-8-*-
import time
import hashlib
import string

db = {}
while True:
    str = raw_input("input employee name and No. split with |:\n,end input with end:\n")
    if "end" == str:
        break;
    key, value = tuple(str.split("|"))
    db[key] = value

print db
if db:
    keys = db.keys()
    keys.sort()
for key in keys:
    print "[%s\t%s]" % (key, db[key])
