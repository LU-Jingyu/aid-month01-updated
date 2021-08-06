"""
练习1：
"""


def somme_chiffres(number):
    """

    :param number:
    :return:
    """
    res = number % 10
    res += number // 10 % 10
    res += number // 100 % 10
    res += number // 1000
    return res


print(somme_chiffres(1234))

