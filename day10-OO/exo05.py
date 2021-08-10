class Enemy:
    def __init__(self, name, life, atk, defence):
        self.name = name
        self.life = life
        self.atk = atk
        self.defence = defence

    def print(self):
        print("姓名：%s，血量：%d，基础攻击力：%d，防御力：%d" %
              self.name, self.life, self.atk, self.damage)


list01 = [
    Enemy("灭霸", 5000, 1000, 800),
    Enemy("玄冥二老", 86, 120, 58),
    Enemy("玄冥三老", 86, 120, 58),
    Enemy("玄冥四老", 86, 1, 58),
]


def find_thanos(str):
    for item in list01:
        if isinstance(item, Enemy):
            if item.name == str:
                return item


# print(find_thanos("灭霸").name)


# 删除攻击力小于10的敌人（倒着删不然可能会错过）
def delete01():
    for i in range(len(list01) - 1, -1, -1):
        if list01[i].atk < 10:
            del list01[i]


delete01()
# print(list01)
