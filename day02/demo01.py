"""
    variable
"""
# 语法：var = expression(变量名称 = 对象)
# 语义：内存图
# 变量名：真实内存地址的别名
# 赋值号：将对象的内存地址复制给左边内存空间
# var1, var2 = str1, str2
# <=> var1 = str1; var2 = str2

#exercise: a = "A"; b = "B"; a = b
#
var1 = input("请输入第一个变量： ")
var2 = input("请输入第二个变量： ")

temp = var1
var1 = var2
var2 = temp
print(var1);print(var2)
