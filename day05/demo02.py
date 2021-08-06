"""
列表内存图
"""
"""# 深拷贝"""
import copy
list01 = [800, [1000, 500]]
list02 = copy.deepcopy(list01)
list01[1][0] = 900
print(list02[1][0])
"""
# 浅拷贝
"""

list03 = list01.copy()
list01[1][0] = 900
print(list03[1][0])


"""
str list 区别
# 需求：根据xx逻辑，拼接一个字符串
# res = “0123456789”

"""
list_temp = []
for item in range(10):
    list_temp.append(str(item))
# join()-->list-->str
res = "".join(list_temp)
print(type(res))
print(res)

"""
str --> list
"""

str_01 = "卢镜宇-谢隽雨-cici-菜菜"
list_res = str_01.split("-")
print(list_res)

