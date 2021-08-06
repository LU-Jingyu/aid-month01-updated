"""
    函数内存图
"""


def fun01(a):
    """
    int是不可变类型
    :param a:
    :return:
    """
    a = 100
    # return a


num = 1
print("num值为：%d" % num)
fun01(num)
print("fun01(num)后为：%d" % num)

"""情况2"""


def fun02(a):
    a[1] = 200


list01 = [1, [2, 3]]
fun02(list01)
print(list01)

"""
    作用域
        glogal:全局作用域
        local:局部作用域
"""
g01 = "OK"


def fun03():
    l01 = 100
    # 定义全局变量g01
    global g01
    # 此时修改的是全局变量
    g01 = "NO"
    print(l01)
    print(g01)


# fun03()
# print(g01)
