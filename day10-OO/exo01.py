"""
"""
import Student
"""
        用学生类来循环录入学生信息
"""
# dict_prod = {}
# while True:
#     nom = input("请输入商品信息： ")
#     if nom == "":
#         break
#     prix = input("请输入商品单价： ")
#     dict_prod[nom] = prix
# for k, v in dict_prod.items():
#     print("商品名：" + k, "单价：" + v)

list_stud = []
while True:
    name = input("请输入学生姓名： ")
    if name == "":
        break
    sex = input("请输入性别： ")
    age = input("请输入年龄： ")
    list_stud.append(Student.Student(name, sex, age))

for item in list_stud:
    item.print()

list_stud[0].print()
