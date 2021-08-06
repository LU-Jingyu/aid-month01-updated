"""
    定义老婆类，创建3个老婆对象
    可以通过类变量记录老婆对象总数
    可以通过类方法打印
"""


class Wife:
    # 类变量
    numbers = 0

    # 类方法
    @classmethod
    def print_wife_amount(cls):
        print(cls.numbers)

    def __init__(self):
        Wife.numbers += 1


w01 = Wife()
w02 = Wife()

Wife.print_wife_amount()
