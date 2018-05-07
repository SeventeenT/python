# 模块时一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能
import sys
import math
import pickle
import pprint

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

# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化
print("常量 PI 的值近似为： {}。".format(math.pi))
print("常量 PI 的值近似为： {!r}。".format(math.pi))
# 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位
print("常量 PI 的值近似为： {0:.3f}。".format(math.pi))
# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {"Google": 1, "Taobao": 2, "Runoob": 3}
for name, number in table.items():
    print("{0:10}==>{1:10d}".format(name, number))

# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值
print("Runoob : {0[Runoob]:d}; Taobao : {0[Taobao]:d}; Google : {0[Google]:d}".format(table))
# 也可以通过在 table 变量前使用 '**' 来实现相同的功能
print("Runoob : {Runoob:d}; Google : {Google:d}; Taobao : {Taobao:d}".format(**table))

print("\n")

# 打开一个文件夹
f = open("D:/test.txt", "w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# 关闭文件
f.close()

# f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
ff = open("D:/test.txt", "r")
str_1 = ff.readline()
print(str_1)
ff.close()

# f.readlines() 将返回该文件中包含的所有行。
# 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割
f3 = open("D:/test.txt", "r")
str_2 = f3.readlines()
print(str_2)
f3.close()

print("\n")
# 另一种方式是迭代一个文件对象然后读取每行
f4 = open("D:/test.txt", "r")
for line in f4:
    print(line, end="")
f4.close()

# f.write(string) 将 string 写入到文件中, 然后返回写入的字符数
f5 = open("D:/test.txt", "w")
num = f5.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
print(num)
f5.close()

# 如果要写入一些不是字符串的东西, 那么将需要先进行转换
f6 = open("D:/test.txt", "a")
value = ('www.runoob.com', 14)
s = str(value)
f6.write(s)
"""
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
  seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
  seek(x,1) ： 表示从当前位置往后移动x个字符
  seek(-x,2)：表示从文件的结尾往前移动x个字符
"""
f6.seek(3, 0)
print(f6.tell())  # f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
f6.close()

# 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短
with open("D:/test.txt", "r") as f7:
    print(f7.read())

print(f7.closed)

print("\n")

# pickle 模块
"""
python的pickle模块实现了基本的数据序列和反序列化。
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
基本接口：pickle.dump(obj, file, [,protocol])
"""
# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4 + 6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open("D:/data.pkl", "wb")
pickle.dump(data1, output)
pickle.dump(selfref_list, output, -1)
output.close()

# 使用pickle模块从文件中重构python对象
pkl_file = open("D:/data.pkl", "rb")
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
data3 = pickle.load(pkl_file)
pprint.pprint(data3)
pkl_file.close()
