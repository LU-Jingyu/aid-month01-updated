"""
练习：将随机列表中大于某个数的所有数字存入一个新的列表
并画出内存图
"""
list01 = [54, 25, 12, 42, 35, 17]
list02 = []
i = 0
for item in list01:
    if item > 30:
        list02.append(item)
        i += 1
        print(list02[i-1])
