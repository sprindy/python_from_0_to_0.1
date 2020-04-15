#!/usr/bin/local/python3
 
import re
m = re.match('run', 'www.runoob.com afdadfadfa', flags=re.I)
if m is not None:
    print(m.group())
else:
    print('not match!')


n = re.search('run', 'www.runoob.com afdadfadfa')
if n is not None:
    print(n.group())
else:
    print('can\'t find!')