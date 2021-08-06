"""
    函数参数
        实际参数

"""


def fun01(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


# 位置实参：实参与实参的位置依次对应
fun01(1, 2, 3, 4)

# 关键字实参：实参与形参
fun01(b=1, d=2, c=3, a=4)

# 序列实参:星号将序列拆分后按位置与形参进行对应
list01 = ["a", "b", "c", "d"]
fun01(*list01)
print("字典实参：")

# 字典实参：双星号将字典拆分后按名称与形参进行对应
dict01 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
fun01(**dict01)


# 4.命名关键字形参（必须命名）
def fun03(*, a, b):
    print(a)
    print(b)


fun03(a="q", b="d")


# 5.字典形参:数量无限的关键字实参
def fun06(**a):
    print(a)


fun06(a=1, b=2)


# 练习：
#     |位置|| 星号元组形参 || 命名关键字 || 双星号字典 |
def fun07(a, b, *args, c, d, **kwargs):
    pass


fun07(3, 4, 5, 6, c=7, d=8, e=9)


# 位置实参无限 + 关键字实参无限
def fun08(*args, **kwargs):
    pass
