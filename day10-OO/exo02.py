import Student

list01 = [
    Student.Student("赵敏", "女", 28),
    Student.Student("苏大强", "男", 68),
    Student.Student("明玉", "女", 30),
    Student.Student("无忌", "男", 29),
]


# 练习1：定义函数，打印指定name如苏大强的名称与年龄
def search_in_list_objet(list_obj, name):
    """
        search by name
    :param list_obj:
    :param name:
    :return:
    """
    for obj in list_obj:
        if isinstance(obj, Student.Student):
            if obj.name == name:
                return obj


# search_in_list_objet(list01, "苏大强").print()


def find_female_list_obj(list_obj):
    """
        find all the female in the giving list
    :param list_obj:
    :return: list of all female
    """
    res = []
    for item in list_obj:
        if isinstance(item, Student.Student):
            if item.sex == "女":
                res.append(item)
    return res


# 输出所有的女同学
# for item in find_female_list_obj(list01):
#     item.print()

def num_age30s_list_obj(list_obj):
    res = 0
    for item in list_obj:
        if isinstance(item, Student.Student):
            if int(item.age) >= 30:
                res += 1
    return res


# print(num_age30s_list_obj(list01))

# 获取list01中所有人的名字
def get_list_name_list_obj(list_obj):
    res = []
    for item in list_obj:
        if isinstance(item, Student.Student):
           res.append(item.name)
    return res
