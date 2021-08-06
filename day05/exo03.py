"""
练习: 录入所有学生的成绩，输入空字符串，打印所有人成绩
    打印最高分，最低分，平均分
"""
list_score = []
while True:
    score_input = input("请输入成绩： ")
    if score_input == "":
        break
    list_score.append(int(score_input))
for item in list_score:
    print(item)
print(max(list_score))
print(min(list_score))
print(sum(list_score) / len(list_score))

