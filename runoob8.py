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

# 对序列里每一个元素调用某个方法
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# strip()移除字符串头尾指定的字符（默认为空格）。
freshfruit_1 = [weapon.strip() for weapon in freshfruit]
print(freshfruit_1)

# 用if子句作为过滤器
vec_if1 = [3 * x for x in vec if x > 3]
print("if过滤器：", vec_if1)
vec_if2 = [3 * x for x in vec if x < 2]
print("if过滤器：", vec_if2)

# 例子
ex1 = [2, 4, 6]
ex2 = [4, 3, -9]
ex3 = [x * y for x in ex1 for y in ex2]
print("两个列表值相乘：", ex3)
ex4 = [x + y for x in ex1 for y in ex2]
print("两个列表值相加：", ex4)
ex5 = [ex1[i] * ex2[i] for i in range(len(ex1))]
print("两个列表相同下标的值相乘：", ex5)

# 列表推导式可以使用复杂表达式或嵌套函数
# round() 返回浮点数的四舍五入值
ex6 = [str(round(335 / 113, i)) for i in range(1, 6)]
print(ex6)

print("\n")

# 嵌套列表解析
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix1 = [[row[i] for row in matrix] for i in range(4)]
print("将3*4的矩阵列表转换为4*3的列表：", matrix1)

print("\n")

# 使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，或清空整个列表
del_a = [-1, 1, 66.25, 333, 333, 1234.5]
del del_a[0]
print("用del删除索引为0的值", del_a)
del del_a[2:4]
print("用del删除索引区间在[2:4]之间的值：", del_a)
del del_a[:]
print("用del清空列表：", del_a)

# 元组由若干逗号分隔的值组成
# 元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的
t = 12345, 54321, "hello!"
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)

print("\n")

"""
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
可以用大括号({})创建集合
注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典
"""
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket)
print("检测成员", "orange" in basket)
print("检测成员", "crabgrass" in basket)

print("\n")

# 以下演示了两个集合的操作
set_a = set("abracadabra")
set_b = set("alacazam")
print("set_a:", set_a)  # set_a 中唯一的字母
print("set_b:", set_b)  # set_b 中唯一的字母
print("set_a - set_b:", set_a - set_b)  # 在set_a中的字母，但是不在set_b中
print("set_a | set_b:", set_a | set_b)  # 在set_a或set_b中的字母
print("set_a & set_b:", set_a & set_b)  # 在set_a和set_b中都有的字母
print("set_a ^ set_b:", set_a ^ set_b)  # 在set_a或set_b中的字母，但不同时在set_a和set_b中

# 集合也支持推导式
set_c = {i for i in "abracadabra" if i not in "abc"}
print("集合推导式：", set_c)

print("\n")
tel = {"jack": 4098, "sape": 4139}
tel["guido"] = 4127
print(tel["jack"])
del tel["sape"]
tel["irv"] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print("guido" in tel)
print("jack" not in tel)

# 字典推导
tel_a = {x: x * 2 for x in (2, 4, 6)}
print("字典推导：", tel_a)
print(tel_a[4])

# 字典遍历  关键字和对应的值可以使用 items() 方法同时解读出来
knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.items():
    print(k, v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(["tic", "tac", "toe"]):
    print(i, v)

print("\n")

# 同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print("What is your {0}? It is {1}.".format(q, a))

print("\n")

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
for i in reversed(range(1, 10, 2)):
    print(i)

print("\n")

# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
vs = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(vs)):
    print(f)


