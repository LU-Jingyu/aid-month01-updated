"""
列表推导式
"""
#
list01 = [5, 6, 7, 8, 9, 0]
# list02 = []
list02 = [item + 1 for item in list01]
# print(list02)

# 使用range生成1-10的数字，将数字的平方存入list01中
list03 = [item**2 for item in range(10)]
list04 = [item for item in list03 if item%2 == 1]
list05 = [item for item in list03 if item%2 == 0]
print(list05, list04)
