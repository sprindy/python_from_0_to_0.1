#!/usr/local/bin/python3

#程序功能： 从1加到100并求和

#定义一个变量放求和的结果，并初始化为0
sum = 0
#定义循环变量并初始化为1
i = 1
#循环执行100次
while (i <= 100):
    sum += i
    i += 1

#打印求和结果
print(sum)

#重新赋值为0
sum = 0
#循环从1加到100
for k in range(1, 101):
    sum += k

#打印求和结果
print(sum)