"""
    字典推导式

"""
# 1 2 3 4 ... 10 au carre
dict01 = {}
for item in range(1, 11):
    dict01[item] = item ** 2

# 推导式
dict02 = {item: item**2 for item in range(1, 11)}
print(dict02)
dict02 = {item: item**2 for item in range(1, 11) if item > 5}
print(dict02)

# 练习：把列表中每个元素及其对应字符串的长度输入字典
list01 = ["卢杰一", "Jay Lu", "Charlie"]
dict01 = {item: len(item) for item in list01}
print(dict01)

# 需求：字典如何根据value查找key
# 方案：键值互换
dict02 = {value: item for item, value in dict01.items()}
print(dict02[3])
