#!/usr/local/bin/python3

import pandas as pd

# 文件名保存到变量里，方便多次使用
file_name = 'students.xlsx'

# 从students.xlsx文件里的Sheet1读取第0行（程序的计数都是从0开始的）
students = pd.read_excel(file_name, header=0, sheet_name='Sheet1')
print(students.columns)
print(students.head())

# 按年龄降序排列
students.sort_values(by='age', ascending=False, inplace=True)
print(students.head())

'''
# 通过假定header=None去手动设置标题
students = pd.read_excel(file_name, header=None)
students.columns = ['id', 'name', 'age']
print(students.columns)
print(students.head())

# 指定id为索引列，默认的0开头的
students2 = pd.read_excel(file_name, index_col='id')
print(students2.head())

# 跳过开头1行，使用“B~C”列数据，设置某些列的类型
studentss = pd.read_excel(file_name, skiprows=1, usecols='B:C',
                          dtype={'id':str, 'name':str, 'age':int})
print(studentss.columns)
print(studentss.head())
'''