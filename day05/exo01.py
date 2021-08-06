"""
day04作业
"""
# long = int(input("请输入边长： "))
long = 4
for item in range(long):
        for i in range(long):
            # 判断是不是行首和行尾
            if item==0 or item==long-1:
                if i==long-1:
                    print("*")
                else:
                    print("*", end="")
            else:#不是行首尾则留空中间，注意第一个竖行不换行
                if i==long-1:
                    print("*")
                elif i==0: print("*", end="")
                else:
                    print(" ", end="")
