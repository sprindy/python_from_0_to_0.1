import re

m = re.split(r'\W+', ' runoob, runoob, runoob.')
if m is not None:
    print('result 1: ', m)

m = re.split(r'(\W+)', ' runoob, runoob, runoob.')
if m is not None:
    print('result 2: ', m)

m = re.split(r'\W+', 'runoob, runoob, runoob.', 1)
if m is not None:
    print('result 3: ', m)

# 匹配至少1个a，对于一个找不到匹配的字符串而言，split 不会对其作出分割
m = re.split(r'a+', 'hello world')
if m is not None:
    print('result 4: ', m)

# 匹配0个或多个的a
m = re.split(r'a*', 'hello world')
if m is not None:
    print('result 5: ', m)
