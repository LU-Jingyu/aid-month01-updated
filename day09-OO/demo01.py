"""
    类与对象
"""


class Girlfriend:
    # member
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    # method
    def play(self):
        """
            一起玩耍
        """
        print(self.name + "玩耍")


# 创建对象， 实际在调用__init__方法
g01 = Girlfriend("Rose","female", 22)#自动将对象地址传入方法
# 调用对象的行为
g01.play()
