#!/usr/local/bin/python3

# 引用模块并起别名
import pandas as pd

df = pd.DataFrame({'ID': [1, 2, 3], \
                   'Name': ['小明', '小强', '晓华'], \
                   'Age': [4, 5, 6]})

print(df)
# 自定义索引（不使用pandas默认的索引），可以注释这句话看log比较差异
df = df.set_index('id')

# 写入到电子表格里
df.to_excel('students.xlsx')

print('Done!')