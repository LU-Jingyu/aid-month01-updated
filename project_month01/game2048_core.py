"""
    需求：
    -->设计：
    -->编码: 2048 游戏核心算法
"""
"""
    如何写在简历里？？？
    降维的思想：从2d变成1d，拆分需求，先实现小需求再合并成大需求
"""
# 1. 零元素移至末尾
#  [2, 0, 2, 0] --> [2, 2, 0, 0]
# [2, 0, 0, 2] --> [2, 2, 0, 0]
# [2, 4, 0, 2] --> [2, 4, 2, 0]

list_merge = [4, 4, 2, 2]


# 1.判断0后有没有元素（从后往前）
# 2.有就交换


def zero_to_end():
    """
        零元素移到末尾
    :param :
    :return:
    """
    for i in range(len(list_merge) - 2, -1, -1):
        if list_merge[i] == 0:
            if list_merge[i + 1] != 0:
                del list_merge[i]
                list_merge.append(0)


def merge():
    """
    先将中间0移至末尾
    再合并相邻相同元素
    :param :
    :return:
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


# merge()
# print(list_merge)

# 练习3：地图向左移动
map = [
    [2, 0, 0, 2],
    [4, 4, 2, 2],
    [2, 4, 0, 4],
    [0, 0, 2, 2]
]


def move_to_left():
    """
        向左移动：将二维列表中每行交给merge函数进行操作
    :return:
    """
    for row in map:
        global list_merge
        list_merge = row
        merge()


def move_to_right():
    for row in map:
        global list_merge
        list_merge = row[::-1]
        merge()
        row[::-1] = list_merge


# move_to_left()
# move_to_right()
# print(map)

# 练习4：向上、向下移动
def diagonal_matrix(list2d):
    """

    :param list2d: 要转置的方阵
    :return:
    """
    for i in range(len(list2d)):
        for j in range(len(list2d[i])):
            if i < j:
                # temp = list2d[i][j]
                # list2d[i][j] = list2d[j][i]
                # list2d[j][i] = temp
                list2d[i][j], list2d[j][i] = \
                    list2d[j][i], list2d[i][j]


def move_to_up():
    """

    :return:
    """
    diagonal_matrix(map)
    for r in range(len(map)):
        global list_merge
        list_merge = map[r]
        merge()
        map[r][:] = list_merge
    diagonal_matrix(map)


def move_to_down():
    """

    :return:
    """
    diagonal_matrix(map)
    for r in range(len(map)):
        global list_merge
        list_merge = map[r][::-1]
        merge()
        map[r][:] = list_merge[::-1]
    diagonal_matrix(map)


# move_to_down()

for item in map:
    print(item)
