"""
    day07作业
    1.打印二维数组
    2.转置方阵
"""



def print_2d_list(list_to_print):
    """

    :param list_to_print: 要打印的2d列表
    :return:
    """
    for item in list_to_print:
        for i in item:
            print(str(i), end=" ")
        print()


list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print_2d_list(list01)


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


diagonal_matrix(list01)
print(list01)
