# -*-coding:utf-8-*-
import time
import hashlib
import string
def translate(map):
    if map:
        dd = {}
        for (key,value) in map.items():
            dd[value] = key
        return dd
if __name__ == '__main__':
    dict1={"key1":"value1"}
    ds ={"map":dict1}
    print translate(**ds)