#!/usr/local/bin/python3

#学生姓名表
students = ['Zhangsan', 'Lisi', '王五']
print('学生姓名表：', students)

#打印学生姓名表
print('第3个学生的姓名是：', students[2])

#修改其中一个学生的姓名
students[1] = "John"
print('学生姓名表：', students)

# 姓名表里追加一个，并打印查看
students.append('Steve')
print('学生姓名表：', students)

# 统计人数，并打印人数
cnt = len(students)
print( 'Students Counter = ' , cnt)

# 删除一个名字，并统计人数还有打印人数
students.remove('Zhangsan')
print('学生姓名表：', students)
print( 'students counter = ' ,len(students))