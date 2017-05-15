# -*- coding:utf-8 -*-
import string

start = raw_input("enter start:")
end = raw_input("enter end:")
start, end = int(start), int(end)
bl = set([chr(x) for x in range(start, end + 1)]) & set(string.printable)
print "DEX\tBIN\tOCT\tHEX\tASCII" if bl else "DEX\tBIN\tOCT\tHEX"
for i in range(int(start), int(end) + 1):
    if bl:
        print "%s\t%s\t%s\t%s\t%s" % (i, bin(i), oct(i), hex(i), chr(i))
    else:
        print "%s\t%s\t%s\t%s" % (i, bin(i), oct(i), hex(i))
