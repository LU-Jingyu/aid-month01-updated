"""
"""
"""
    封装
        使用属性property（读取方法，写入方法），封装变量
"""


class Wife:
    def __init__(self, name, age=None, weight=None):
        # 变量私有化
        self.name = name
        self.__weight = weight
        self.__age = age

    @property #创建property对象，只负责拦截读取操作
    def age(self):
        return self.__age

    @age.setter #只负责拦截写入操作
    def age(self, age):
        # 控制语句
        if 21 <= age <= 30:
            self.__age = age
        else:
            raise ValueError("我不要")

    # property对象拦截对age类变量的读写操作
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if 40 <= weight <= 80:
             self.__weight = weight
        else:
            raise ValueError("error")


w01 = Wife("xjy")
w01.weight = 45
w01.age = 22
print(w01.__dict__)
# print(w01.age())
