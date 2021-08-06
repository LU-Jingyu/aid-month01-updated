"""
    集合
"""
# 1.创建
set01 = set()
set01 = set("abcac")
# 转列表
list01 = list(set01)
print(set01)
print(list01)
# 转字符串
str01 = "".join(list01)
print(str01)
# 2.添加
set01.add("ljy")
print(set01)
# 3.删除
set01.remove("a")
# 4.获取元素
for item in set01:
    print(item)

# ***5. 数学运算
# 交集
set01 = {2, 3, 4}
set02 = {2, 3, 1}
print(set02 & set01) #{2, 3}
# 并集
print(set01 | set02) #{1, 2, 3, 4}
# 补集
print(set01 ^ set02)#{1, 4}
#子集
set03 = {1, 2}
print(set03 <= set02)
#超集
print(set02 > set03)

# 练习：打入字符串，输入空字符串停止并打印不重复的文字
set04 = set()
while True:
    str02 = input("...:")
    if str02 == "":
        break
    set04.add(str02)
print(set04)
