import random
import unicodedata

# 随机生成0~9的数
# random.randint(a, b)  函数返回数字 N ，N 为 a 到 b 之间的数字（a <= N <= b），包含 a 和 b。
print(random.randint(0, 9))

# 摄氏温度转华氏温度的公式为 celsius * 1.8 = fahrenheit - 32
a = int(input("摄氏度转为华氏温度请按1\n华氏温度转化为摄氏度请按2\n"))
while a != 1 and a != 2:
    a = int(input("你选择不正确，请重新输入。\n摄氏度转为华氏温度请按1\n华氏温度转化为摄氏度请按2\n"))
if a == 1:
    celsius = float(input("请输入摄氏度：\n"))
    fahrenheit = (celsius * 1.8) + 32  # 计算华氏温度
    print("%.1f摄氏度转为华氏温度为%.1f" % (celsius, fahrenheit))
else:
    fahrenheit = float(input("请输入华氏温度：\n"))
    celsius = (fahrenheit - 32) / 1.8
    print("%.1f华氏温度转化为摄氏度为：%.1f" % (fahrenheit, celsius))


# 判断字符串是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 测试字符串和数字
print(is_number("foo"))
print(is_number("1"))
print(is_number("1.3"))
print(is_number("-1.37"))
print(is_number("1e3"))  # 1  数字1

# 测试 Unicode
print(is_number("٥"))  # 阿拉伯语  5
print(is_number("๒"))  # 泰语  2
print(is_number("四"))  # 中文数字  4
print(is_number("©"))  # 版权号

# 判断奇偶数
while 1 > 0:
    try:
        num = int(input("请输入一个数字\n"))
    except ValueError:
        print("输入的不是整数！")
        continue
    if num % 2 == 0:
        print("偶数")
    else:
        print("奇数")
    break
