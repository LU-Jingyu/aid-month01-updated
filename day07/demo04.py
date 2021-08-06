"""
    列表推导式嵌套
"""

"""
    def function():
    
"""


def rectangle(long, char):
    for item in range(long):
        for i in range(long):
            # 判断是不是行首和行尾
            if item == 0 or item == long - 1:
                if i == long - 1:
                    print(char)
                else:
                    print(char, end="")
            else:  # 不是行首尾则留空中间，注意第一个竖行不换行
                if i == long - 1:
                    print(char)
                elif i == 0:
                    print(char, end="")
                else:
                    print(" ", end="")


rectangle(4, "@")
