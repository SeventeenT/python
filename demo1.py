import cmath
import math

# 用户输入两个数字 求和
num1 = input("请输入一个数字：")
num2 = input("请再输入一个数字：")
sum1 = float(num1) + float(num2)
print("数字 {0} 和数字 {1}的和为 {2}".format(num1, num2, sum1))

# 合并
# print("两数之和为：%.1f" % (float(input("请输入一个数字：")) + float(input("请再输入一个数字："))))

# 平方根，又叫二次方根，表示为〔√￣〕，如：数学语言为：√￣16=4。语言描述为：根号下16=4。
num3 = float(input("请输入一个数字："))
# 这个方法只适用于正数。
# num_sqrt = num3 ** 0.5
# print("%.3f的平方根为%.3f" % (num3, num_sqrt))
# 负数和复数可以使用以下的方式
num_sqrt = cmath.sqrt(num3)
print("{0}的平方根为{1}".format(num3, num_sqrt))

# 二次方程式 ax**2 + bx + c = 0
# 输入a、b、c
# 输出 x 的解
# x1=(-b+sqrt(b**2-4ac))/2a
# x2=(-b-sqrt(b**2-4ac))/2a

a = float(input("a为："))
b = float(input("b为："))
c = float(input("c为："))
# 计算得到d
d = b ** 2 - 4 * a * c
print("d的值为{0}".format(d))
if d == 0:
    x = -b / 2 * a
    print("x的值为{0}".format(x))
elif d > 0:
    x1 = -b + math.sqrt(d) / 2 * a
    x2 = -b - math.sqrt(d) / 2 * a
    print("x1的值为{0},x2的值为{1}".format(x1, x2))
else:
    x1 = -b + cmath.sqrt(d) / 2 * a
    x2 = -b - cmath.sqrt(d) / 2 * a

# 计算半周长
s = (a + b + +c) / 2
# 计算面积
area = math.sqrt((s * (s - a) * (s - b) * (s - c)))
print("三角形的面积为：%.2f" % area)
