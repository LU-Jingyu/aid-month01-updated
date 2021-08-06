"""
    定义列表排序函数
"""


# 使用交换排序
def swap_sort(list_to_sort):
    # 传入的是可变的对象

    for i in range(len(list_to_sort) - 1):
        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[i] > list_to_sort[j]:
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[j]
                list_to_sort[j] = temp


list01 = [3, 80, 45, 5, 80, 80]
swap_sort(list01)
print(list01)
