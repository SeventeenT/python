# coding=utf-8
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter, miles, name)

# 多个变量赋值
a = b = c = 1  # 创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。
d, e, f = 1, 2, "runoob"  # 为多个对象指定多个变量。
print(a, b, c, d, e, f)

# 六个标准数据类型
# 不可变数据（四个）：Number(数字)，String(字符串)，Tuple(元组)，Sets(集合)
# 可变数据（两个）：List(列表)，Dictionary(字典)

# Number(数字)
# Python3支持 int、float、bool、complex(复数)
# 内置的type()函数可以用来查询变量所指的对象类型
aa, bb, cc, dd = 20, 5.5, True, 4 + 3j
print("aa==", type(aa), ",bb=", type(bb), ",cc=", type(cc), ",dd=", type(dd))
# 也可以用isinstance来判断
print(isinstance(aa, int))
# del 删除一些对象引用

print("~" * 30)

# 数值运算
print("加法 =", 5 + 4)
print("减法 = ", 4.3 - 2)
print("乘法 = ", 3 * 7)
print("除法 = ", 2 / 4)  # 除法，得到一个浮点数
print("除法 = ", 13 // 4)  # 除法，得到一个整数
print("取余 = ", 17 % 3)
print("乘方 = ", 2 ** 5)

print("~" * 30)

# 列表
'''
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号([])之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
'''
list1 = ["abcd", 786, 2.23, "runoob", 70.2]
tiny_list = [123, "runoob"]

print("输出完整列表：", list1)
print("输出列表第一个元素：", list1[0])
print("从第二个开始输出到第三个元素：", list1[1:3])
print("输出从第三个元素开始的所有元素：", list1[2:])
print("倒序:", list1[::-1])
print("输出两次列表：", tiny_list * 2)
print("链接列表：", list1 + tiny_list)

# 列表中的元素是可变的
list_a = [1, 2, 3, 4, 5, 6]
list_a[0] = 9
list_a[2:5] = [13, 14, 15]
print(list_a)

print("~" * 30)

# Tuple(元组)
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
tuple_a = ("abcd", 789, 2.23, "runoob", 70.2)
tiny_tuple = (123, "runoob")
print("输出完整元组：", tuple_a)
print("输出元组的第一个元素：", tuple_a[0])
print("输出从第二个元素开始到第三个元素：", tuple_a[1:3])
print("输出从第三个元素开始的所有元素：", tuple_a[2:])
print("倒序：", tuple_a[::-1])
print("输出两次元素：", tiny_tuple * 2)
print("连接元组：", tuple_a + tiny_tuple)

#
list2 = [1, 2, 3]
list3 = [4, 5, 6]
# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
tuple1 = (1, list2, list3)
tuple2 = (0,)  # 一个元素，需要在元素后添加逗号
print(tuple1 + tuple2)

print("~" * 30)

# Set 集合
# 集合（set）是一个无序不重复元素的序列。基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
parame = {"value1", "value2", "value3", "value4", "value5", "value5"}
# 成员测试
if "value1" in parame:
    print("value1在集合中")
else:
    print("value1不在集合中")
print(parame)  # 无序的   输出时重复元素会被自动去掉
set1 = set("123456")
print(set1)

# set可以进行集合运算
q = set("abracadabra")
w = set("alacazam")
print("集合q =", q)
print("集合w =", w)
print("q和w的差集 =", q - w)
print("q和w的并集 =", q | w)
print("q和w的交集 =", q & w)
print("q和w中不同时存在的元素 =", q ^ w)

print("~" * 30)

# Dictionary (字典)
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
dict = {}
dict["one"] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tiny_dict = {"name": "runoob", "code": 1, "site": "www.runoob.com"}
print("输出键为“one”的值:", dict["one"])
print("输出键为2的值:", dict[2])
print("输出完整的字典:", tiny_dict)
print("输出所有键:", tiny_dict.keys())
print("输出所有值:", tiny_dict.values())

# 字典类型也有一些内置的函数，例如clear()、keys()、values()等。
# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。
