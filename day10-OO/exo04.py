"""
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"]
]
在二维列表里，获取（1，3）位置，向左， 3个元素
"""
import demo04

list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"]
]


vect01 = demo04.Vector2(1, 3)
vect02 = demo04.Vector2(2, 2)


res = demo04.DoubleListHelper.get_elements(list01, vect01, demo04.Vector2.left(), 3)
print(res)
res = demo04.DoubleListHelper.get_elements(list01, vect02, demo04.Vector2.up(), 2)
print(res)
