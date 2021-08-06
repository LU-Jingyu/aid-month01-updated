sum = 0
# for item in range(10,51):
#     unit = item % 10
#     if unit !=2 or unit!=5 or unit !=7:
#         sum += item
# print(sum)

"""
练习1：在控制台输入一个字符串，然后打印每个字符的编码值
"""
str = input("give a string: ")

# print(chr(256))
for i in str:
    print(ord(i))

"""
练习2：在控制台输入一个编码值，输出对应的字符，空字符串则退出程序
"""
while True:
    str_code = input("请输入编码值： ")
    if str_code =="": break
    value = int(str_code)
    print(chr(value))
