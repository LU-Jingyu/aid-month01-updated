"""
        字典dict
"""
# 1.创建
dict01 = {}
dict01 = dict()

dict01 = {"wj":100, "zm":80, "zr":90}
print(dict01)
# 查找（key --> value）
print(dict01["wj"])
# 修改、添加元素
dict01["a"] = "BB"
print(dict01)
# 删除元素
del dict01["a"]
# print(dict01)
# 遍历
for key in dict01:
    print(key, end=": ")
    print(dict01[key])

for k, v in dict01.items():
    print(k, v)
