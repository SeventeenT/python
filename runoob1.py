# coding=utf-8
# 基础语法
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *

import keyword
import sys
from sys import argv, path

print("path:", path)
print("argv:", argv)

print(keyword.kwlist)
# 第一个注释
'''
多行注释可以用多个#，
还有''' '''和 """ """
'''
""" 多行注释"""

print("Hello,World!")

# 缩进
# python最具特色的就是使用缩进来表示代码块，不需要使用{ }
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进格数
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")  # 缩进不一致，会导致运行错误

# Python 通常是一行写完一条语句，如果语句很长，我们可以用反斜杠\来实现多行语句   直接回车系统会自动生成\
total = "item_one " + \
        "item_two " + \
        "item_three"
# 在[] { } 或 () 中的多行语句不需要使用反斜杠\
totals = ['item_one',
          'item_two',
          'item_three']
print(total, totals)

# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
print("不使用r，反斜杠发生转义：this is a line with \n a")
print(r"使用r，反斜杠不发生转义：this is a line with \n a")

# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
print("this " + "is " + "a")
print("*运算符重复：" + "a" * 10 + "\n")

# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python中的字符串不能改变。

# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串的截取的语法格式如下：
aa = "runoob"
print("输出字符串：" + aa)  # 输出字符串
print("输出第一个到倒数第二个的所有字符：" + aa[0:-1])  # 输出第一个到倒数第二个的所有字符
print("输出字符串第一个字符：" + aa[0])  # 输出字符串第一个字符
print("输出从第三个开始到第五个的字符：" + aa[2:5])  # 输出从第三个开始到第五个的字符
print("输出从第三个开始的后面的所有的字符：" + aa[2:])  # 输出从第三个开始的后面的所有的字符
print("输出字符串两次：" + (aa + " ") * 2)  # 输出字符串两次
print("连接字符串：" + aa + " 你好")  # 连接字符串
print("倒序：" + aa[::-1])

print("---" * 20)

# 等待用户输入
# input("\n 按下 enter 键后退出\n")

# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割   （系统格式化会自动换行）
x = "runoob"
sys.stdout.write(x + "\n")

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x = "a"
y = "b"
print("不换行输出" + x, end=" ")
print(y)
