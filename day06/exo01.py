"""
练习1：在控制台中录入商品信息（名称及单价）
    如果输入空字符串，则停止录入
    将所有信息逐行打印
"""
dict_prod = {}
# while True:
#     nom = input("请输入商品信息： ")
#     if nom == "":
#         break
#     prix = input("请输入商品单价： ")
#     dict_prod[nom] = prix
# for k, v in dict_prod.items():
#     print("商品名："+k, "单价："+v)

# 练习2：录入学生信息（姓名，性别，年龄，成绩）
"""
# 字典内嵌字典
{
    "卢杰一"：{"sex": man,"age": 21,"score": 12}
}
"""
dict_stud = {}
while True:
    nom = input("请输入学生姓名： ")
    if nom == "":
        break
    genre = input("请输入性别： ")
    age = input("请输入年龄： ")
    note = input("请输入成绩： ")
    dict_stud[nom] = {"sex": genre, "age": age,"score": note}
for k, v in dict_stud.items():
    print("name: "+k, "性别："+v["sex"],
          "年龄："+v["age"],
          "成绩： "+v["score"])

