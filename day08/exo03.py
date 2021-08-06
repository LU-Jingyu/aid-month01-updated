"""
    字符串常用函数：
"""
str_01 = " 校 训：自 强不息、厚德载物。  "
print(str_01.count(" "))
print(str_01.lstrip())
# print(str_01.rstrip())
str_01 = str_01.strip(" ")
# print(str_01)
str_01 = str_01.split(" ")
# print(str_01)
str_01 = "".join(str_01)
print(str_01)

