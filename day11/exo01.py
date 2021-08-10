class Enemy:
    def __init__(self, name, life, atk, defence):
        self.name = name
        self.life = life
        self.atk = atk
        self.defence = defence

    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, life):
        self.__life = life

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if value >= 30:
            self.__atk = value
        else:
            raise ValueError("error")

    def print(self):
        print("姓名：%s，血量：%d，基础攻击力：%d，防御力：%d" % (self.name, self.__life, self.__atk, self.defence))


e01 = Enemy("灭霸", 100, 30, 200)
# e01.atk = 29
print(e01.__dict__)
