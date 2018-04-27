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

# 数值运算
print("加法 =", 5 + 4)
print("减法 = ", 4.3 - 2)
print("乘法 = ", 3 * 7)
print("除法 = ", 2 / 4)  # 除法，得到一个浮点数
print("除法 = ", 13 // 4)  # 除法，得到一个整数
print("取余 = ", 17 % 3)
print("乘方 = ", 2 ** 5)

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
print("输出两次列表：", tiny_list * 2)
print("链接列表：", list1 + tiny_list)

# 列表中的元素是可变的
list_a = [1, 2, 3, 4, 5, 6]
list_a[0] = 9
list_a[2:5] = [13, 14, 15]
print(list_a)

# Tuple(元组)
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
tuple_a = ("abcd", 789, 2.23, "runoob", 70.2)
tiny_tuple = (123, "runoob")
print("输出完整元组：", tuple_a)
print("输出元组的第一个元素：", tuple_a[0])
print("输出从第二个元素开始到第三个元素：", tuple_a[1:3])
print("输出从第三个元素开始的所有元素：", tuple_a[2:])
print("输出两次元素：", tiny_tuple * 2)
print("连接元组：", tuple_a + tiny_tuple)
