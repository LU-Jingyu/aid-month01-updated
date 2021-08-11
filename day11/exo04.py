"""
    张无忌 教 赵敏 九阳神功
    赵敏 教 张无忌 化妆
    张无忌 上班 挣了 1w
    思考：变化点是数据的不同还是行为的不同
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

    def teach(self, person, what=None):
        if isinstance(person, Person) and isinstance(what, Action):
            print(self.name+"教"+person.name + what.name)
        else:
            raise ValueError("typeError")

    def work(self, money=0):
        if money > 0:
            print(self.__name+"上班挣了"+str(money))
        else:
            print(self.__name+"上班")


class Action:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


zhang = Person("张无忌")
jiuYang = Action("九阳神功")
zhao = Person("赵敏")

zhang.teach(zhao, jiuYang)
zhang.work(10000)
