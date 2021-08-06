#随机数小游戏
# 随机数工具
import random
# 产生一个随机数
random_num = random.randint(1, 100)
while True:
        num = int(input("enter a number: "))
        if num<random_num:
            print("小了")
        elif num>random_num:
            print("大了")
        else:
            print("你猜对了！")
            break
