"""
    练习：在控制台中录入多个人的喜好

"""
"""
{
    "张三"：[”爱好1“，”爱好2“， ”爱好3“]
}
"""
dict_01 = {}

while True:
    name = input("请输入姓名：")
    if name == "":
        break
    # dict_01[name] = []
    list_hobby = []
    while True:
        hobby = input("请输入爱好：")
        if hobby == "":
            break
        list_hobby.append(hobby)
    dict_01[name] = list_hobby

for k, value in dict_01.items():
    print("姓名：%s 爱好：" % k, end=" ")
    for item in value:
        print(item, end="，")
