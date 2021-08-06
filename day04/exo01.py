# 一张纸对折几次可以超过珠穆朗玛峰
# 纸张厚度为0.01mm，珠峰高8848m
count=0
paper_height=1e-05
while paper_height<=8848.0:
    count+=1
    paper_height*=2
print(count)
