# -*- coding:utf-8 -*-

import string
import keyword

alphas = string.letters + '_'
nums = string.digits
print alphas
print 'welcom to the identifier checker v1.0'
print 'Testees must be at least 2 chars long.'
myinput = raw_input('Identifier to test? ')
valid = True
if keyword.iskeyword(myinput):
    pass
else:
    if myinput[0] not in alphas:
        print """invalid :
                    first symbol must be alphaetic"""
        valid = False
    if len(myinput) > 1:
        for otherChar in myinput[1:]:
            if otherChar not in alphas + nums:
                print """invalid:
                                symbols must be alphanumeric"""
                valid = False
                break


if valid:
    print "okay as an identifier"
