# 模块时一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能
import sys
import site

sys.ps1 = "C>"

for i in sys.argv:
    print("===", i)

print("路径为：", sys.path)

if __name__ == "__main__":
    print("程序自身在运行")
else:
    print("我来自另一模块")

# 内置的函数dir()可以找到模块内定义的所有名称。以一个字符串列表的形式返回
# a = [1, 2, 3, 4, 5]
# b = sys.flags
print(dir())
a = 5
print(dir())
del a  # 删除a
print(dir())

s = "Hello World!"
print(str(s))
print(repr(s))
x = 10 * 3.25
y = 200 * 200
# s = "x的值为：" + repr(x), "y的值为：" + repr(y) + "..."
s = "x的值为：" + repr(x), "y的值为：" + repr(y) + "..."
print(s)

# repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)
# repr()的参数可以是Python的任何对象
print(repr((x, y, ("Google", "Runoob"))))

print("\n")
# 输出一个平方与立方的表
# 第一种方法
print("第一种方法：")
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=" ")
    print(repr(x * x * x).rjust(4))

# 第二种方法
print("第二种方法：")
# 0 代表x,:2d 表示两个宽度的10进制数显示。
# 1 代表x*x,:3d 表示三个宽度的10进制数显示。
# 2 代表x*x*x,:4d 表示四个宽度的10进制数显示。
for x in range(1, 11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x * x, x * x * x))

print("\n")

print("{}网址：“{} ！”".format("菜鸟教程", "www.runoob.com"))
print("{0},{1}".format("Google", "Runoob"))
print("{name}网址：“{site} ！”".format(name="菜鸟教程", site="www.runoob.com"))
print("站点列表{0},{1},和{other}".format("Google", "Runoob", other="Taobao"))
