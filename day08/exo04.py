"""
    判断一个数是不是素数
"""


def isPremier(number):
    """

    :param number:
    :return:True则是素数， False则不是
    """
    if number == 1 or number < 1:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0: return False
    return True


def get_premier(begin, end):
    """

    :param begin:
    :param end:
    :return: 指定范围内的素数list
    """
    list_prime = []
    for number in range(begin, end):
        if isPremier(number):
            list_prime.append(number)
    return list_prime


# num = eval(input("please enter a number to tell if it's prime number: "))
# print(isPremier(num))
list01 = get_premier(1, 100)
print(list01)
