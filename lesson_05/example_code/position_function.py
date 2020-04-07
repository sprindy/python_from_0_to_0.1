#!/usr/bin/python3

#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return

#调用printinfo函数
# 每个参数都赋值
printinfo( age=50, name="Sprindy" )
print ("------------------------")
# 传递1个参数，并对其中一个参数赋值
printinfo( name="Sprindy" )
print ("------------------------")
# 传递2个参数，并指定对其中一个参数赋值
printinfo( 20, age="Sprindy" )
print ("------------------------")
# 传递2个参数，都不指定的赋值
printinfo( 20, "Sprindy")