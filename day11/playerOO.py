"""

"""


class Player:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if value >= 30:
            self.__atk = value
        else:
            raise ValueError("error")

    def attack(self, other):
        # 进攻的逻辑
        print("攻击")
        if isinstance(other, Enemy):
            other.damage(self.__atk)

    def damage(self, value):
        """

        :param value:
        :return:
        """
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    # 私有的死亡方法
    @staticmethod
    def __death():
        print("player is dead.")
        print("Game over...")


class Enemy:
    def __init__(self, name, life, atk, defence):
        self.name = name
        self.life = life
        self.atk = atk
        self.defence = defence

    def __del__(self):
        print("enemy " + self.name + " is dead.")

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

    def damage(self, value):
        self.__life -= value
        if self.__life <= 0:
            self.__death()

    # 私有的死亡方法
    def __death(self):
        self.__del__()

    def attack(self, player):
        player.damage(self.__atk)


player = Player(100, 100)
e01 = Enemy("e01", 100, 100, 20)

player.attack(e01)
e01.attack(player)
