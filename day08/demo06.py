"""
    函数参数
        形式参数
"""


# 默认参数：如果实参不提供，可以使用默认值
def fun01(a=0, b=0, c=0, d=0):
    print(a)
    print(b)
    print(c)
    print(d)


# 关键字实参+默认形参：可随意调用参数
# fun01(b=2, c=3)

"""
# 
"""


def get_ss_by_hh_mm_ss(h=0, m=0, s=0):
    """
    练习：定义函数，根据时、分、秒计算总秒数
    H, M, S --> S
    H --> s
    min --> s
    H, min --> s
    H, s --> s
    :param h: hour
    :param m: minute
    :param s: second
    :return: seconds in total
    """
    ss = 0
    if h != 0: ss += 3600 * h
    if m != 0: ss += 60 * m
    if s != 0: ss += s
    return ss

print(get_ss_by_hh_mm_ss(h=1,s=40))
