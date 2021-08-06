"""
    ***
    ***
    ***
"""
for l in range(4):
    for c in range(6):
        if c % 2 == 1:
            print("#", end="")
        else:
            print("*", end="")
    print()
print("\n")
for l in range(4):
    for c in range(l + 1):
        print("*", end="")
    print()

"""
    升序排序
"""
list01 = [3, 80, 45, 5, 80, 80]
# 使用交换排序
for i in range(len(list01) - 1):
    for j in range(i + 1, len(list01)):
        if list01[i] > list01[j]:
            temp = list01[i]
            list01[i] = list01[j]
            list01[j] = temp

print(list01)

# 判断是否有两个相同元素，有则返回相同值
res = False
for i in range(0, len(list01) - 1):
    for j in range(i + 1, len(list01)):
        if res:
            break
        if list01[i] == list01[j]:
            print(list01[i])
            res = True
            break
if res is False:
    print("nope")

# 将二维列表的行变成列，列变成行
list02 = [
    [1,2,3,4],
    [5,6,7,8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
res = []
for c in range(4):
    res.append([])
    for r in range(len(list02)):
        res[c].append(list02[r][c])
print(res)
