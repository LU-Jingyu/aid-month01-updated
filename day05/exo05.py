"""
练习：彩票 双色球：
"""
"""
红球：7个，1~33之间的整数（不允许重复）
蓝球：1个，1~17之间的整数
1.随机生成一注彩票【7+1】
2.在控制台购买一张彩票，并开奖
"""
import random

list_num = []
while len(list_num) < 7:
    num = random.randint(1, 33)
    if len(list_num) != 7:
        if num not in list_num:
            list_num.append(num)
    # 蓝球
    else:
        list_num[6] = random.randint(1, 16)
print(list_num)
# 输入
