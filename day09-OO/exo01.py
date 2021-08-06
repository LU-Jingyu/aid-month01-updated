"""
    day09作业：
        1.复习2048核心算法，编写消消乐游戏
        2.购物车改为对象
        3.创两个类，四个对象，并调用其方法

"""


class Laptop:
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    def demarrer(self):
        print("Ur laptop is turing on.")

    def eteindre(self):
        print("Ur laptop is turing off.")


class Monitor:
    def __init__(self, size, brand):
        self.size = size
        self.brand = brand

    def brancher(self):
        print("Ur monitor is power up.")
