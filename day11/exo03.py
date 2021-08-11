"""
    小明在招商银行取钱
"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class Bank:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def draw_money(self, person):
        print("%s在%s取钱" % (person, self.__name))


ming01 = Person("小明")
bank01 = Bank("招商银行")

bank01.draw_money(ming01.name)
