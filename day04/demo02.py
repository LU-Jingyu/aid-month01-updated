'''
    索引，切片
'''
# message = "宇宙第一帅"
# # 获取第三个字
# print(message[2])
# print(message[-1])
# print(message[2 : 4])
# print(message[:])
# print(message[::-1])

"""
练习：在控制台中获取一个字符串
打印第一个，最后一个，倒数第三个，前两个，倒序
如果字符串为奇数则打印中间字符
"""
str = input("请输入一个字符串： ")
print(str[0])
print(str[-1])
print(str[-3])
print(str[:2])
print(str[::-1])
if len(str) % 2==1:
    print(str[int(len(str)/2)])
