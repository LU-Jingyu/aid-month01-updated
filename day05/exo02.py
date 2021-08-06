"""
判断字符串是否为回文
"""
# str = input("请输入字符串： ")
str = "上海自来水来自海上"
i=0
j=len(str)-1
while i<=j:
    if str[i]!=str[j]:
        print("不是回文")
        break
    i+=1
    j-=1
else:
    print("是回文")

# 切片
'''
if str == str[::-1]:
    print("是回文")
else:
    print("不是回文")'''
