class Student:
    def __init__(self, name, sex, age):
        self.sex = sex
        self.name = name
        self.age = age

    def print(self):
        print("Hi, 我叫" + self.name, "性别："+self.sex,
              "年龄："+str(self.age))
