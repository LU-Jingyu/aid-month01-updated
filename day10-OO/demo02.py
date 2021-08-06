"""
    类成员、类变量
"""


class ICBC:
    """
        工商银行
    """
    # 表示总行的钱
    total_money = 1000000

    def __init__(self, name, money):
        self.name = name
        self.money = money
        ICBC.total_money -= money

    @classmethod
    def print_total_money(cls):
        print(cls.total_money)


i01 = ICBC("广渠门支行", 100000)
i02 = ICBC("陶然亭支行", 100000)
print("总行还剩%dw元" % ICBC.total_money)
