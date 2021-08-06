"""
元组--
    基础操作
"""
#创建

# 获取
tup01 = ("a", "b", "c", "d")
# 通过索引
e01 = tup01[1]
# 通过切片
e02 = tup01[-2:]

# 可以直接将元组赋值给多个变量
tup02 = (100, 200)
a, b = tup02
# print(a, b)

"""
练习：输入日期转天数
如：3月5日 == 31+28+5天
"""
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int(input("请输入月份："))
day = int(input("请输入日： "))
totalDay = sum(day_of_month[:month-1]) + day
print(totalDay)
