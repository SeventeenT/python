# Fibonacci series:斐波那契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b, end=", ")
    a, b = b, a + b

print("\n")
# 条件控制
var1 = 100
if var1:
    print("var1为true")
    print("var1 =", var1)

var2 = 0
if var2:
    print("var2为true")
    print(var2)
print("Good bye!")

print("=" * 30)

# if 实例
age = int(input("请输入你家狗狗的年龄："))
print("")
if age < 0:
    print("你是在逗我吧")
elif age == 1:
    print("相当于14岁的人")
elif age == 2:
    print("相当于22岁的人")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄：", human)
# 提示退出
# input("点击enter键退出")

# 数字猜谜游戏实例
number = 7
guess = -1
print("数字猜谜游戏！")
while number != guess:
    guess = int(input("请输入你猜的数字：\n"))
    if number == guess:
        print("恭喜你猜对了！")
    elif number > guess:
        print("数字猜小了...")
    elif number < guess:
        print("数字猜大了...")

# if 嵌套实例
num = int(input("请输入一个数字：\n"))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除 2 和 3 ")
    else:
        print("你输入的数字可以整除 2，但不能整除 3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除 3，但不能整除 2")
    else:
        print("你输入的数字不可以整除 2 和 3")
