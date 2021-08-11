"""
    封装设计思想
        需求：老张开车去东北
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

    def go_to(self, tool, place):
        print("%s开%s去%s" % (self.__name, tool, place))


class Tool:
    def __init__(self, type):
        self.type = type

    def go_to(self, person, place):
        print("%s开%s去%s" % (person, self.type, place))


zhang01 = Person("老张")
car01 = Tool("车")
car01.go_to(zhang01.name, "东北")
