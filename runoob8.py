# 函数
"""
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""


def hello():
    print("Hello World!")


hello()


# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("welcome", name)


print_welcome("Runoob")
w = 4
h = 5
print("width =", h, "height =", h, "area =", area(w, h))


def print_info(name, age):
    print("年龄：", age)
    print("名字：", name)
    return


print_info(age=34, name="Lucy")

print("=" * 30)


# 不定长参数
def print_length(arg1, *vartuple):
    # 打印任何传入参数
    print("输出：")
    print(arg1)
    for var in vartuple:
        print(var)
    return


print_length(10)
print_length(10, 20, 30)

# lambda 函数
# lambda [arg1 [,arg2,.....argn]]:expression

sum = lambda arg1, arg2: arg1 + arg2

print("相加后的值：", sum(10, 20))
print("相加后的值：", sum(20, 20))


# return
def sum1(arg1, arg2):
    totle = arg1 + arg2
    print("函数内：", totle)
    return totle


totle = sum1(10, 20)
print("函数外：", totle)

print("*" * 30)

# global 和 nonlocal关键字
# 修改全局变量num
num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)


fun1()
print(num)

print("*" * 30)


# 修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字
def outer():
    num = 10

    def inner():
        nonlocal num
        num = 100
        print(num)

    inner()
    print(num)


outer()

list_a = [0, 1, 2, 3]
list_a.reverse()  # 倒叙列表
print("倒叙", list_a)

vec = [2, 4, 6]
vec_3 = [3 * x for x in vec]
print("列表推导式", vec_3)
vec_4 = [[x, x * 2] for x in vec]
print(vec_4)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# strip()移除字符串头尾指定的字符（默认为空格）。
freshfruit_1 = [weapon.strip() for weapon in freshfruit]
print(freshfruit_1)
