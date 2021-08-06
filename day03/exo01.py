# day02作业

# accelerated_speed = int(input("请输入加速度a： "))
# time = int(input("time: "))
# print(accelerated_speed * time**2 * 0.5)

# del语句：删除变量,同时解除与对象的关联，可能释放对象
a = "悟空"
b = a
c = a
del a,b
c = None #自动内存管理，释放对象“悟空”

# 拓展练习 秒转化成HHMMSS
total_seconds = int(input("seconds: "))
second = total_seconds % 60
hour = total_seconds // 3600
minute = total_seconds 
