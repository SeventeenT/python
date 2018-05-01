import random

a = 2.2
print(int(a))
b = 3
c = 6.23412
print(float(b))
# round(x,n)四舍五入,n-小数点后几位
print(round(c, 3))

# 从0-9随机挑选一个整数
d = random.choice(range(10))
print(d)

# 将序列里的所有元素随机排序
list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(list_1)
print(list_1)
