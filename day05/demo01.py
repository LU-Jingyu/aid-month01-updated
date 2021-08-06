"""
    列表
"""
list02 = ["1","2","3","4","5"]
# 查询元素
print(list02[0:])
print(len(list02))
# 删除元素
list02.remove("2")
# 切片
print(list02[0:])

# 遍历列表
for item in list02:
    print(item, end="")
print('')
# 倒序遍历列表
for item in range(-1,-len(list02)-1,-1):
    print(list02[item], end="")
