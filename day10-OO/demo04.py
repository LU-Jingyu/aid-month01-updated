"""
    静态方法

    总结：
        实例方法：操作对象的变量
        类方法：操作类的变量
        静态方法：既不需要操作实例变量也不需要操作类变量

"""
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"]
]


class Vector2:
    """
        二维向量
        可以表示位置、方向
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 将函数移入类中
    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)


class DoubleListHelper:
    @staticmethod
    def get_elements(target, vect_pos, vect_dir, count):
        """

        :param target: list2d
        :param vect_pos:
        :param vect_dir: left()/right()...
        :param count:
        :return:
        """
        res = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            res.append(target[vect_pos.x][vect_pos.y])
        return res


pos01 = Vector2(1, 1)

pos01.x += Vector2.left().x
pos01.y += Vector2.left().y
# pos01 += right()
# print(pos01.x, pos01.y)
# print(DoubleListHelper.get_elements(list01,  Vector2(1, 3),Vector2.left(), 2))
