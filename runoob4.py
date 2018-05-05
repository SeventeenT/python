import random

a = 2.2
print(int(a))
b = 3
c = 6.23412
print(float(b))
# round(x,n)四舍五入,n-小数点后几位
print(round(c, 3))

# 从0-9随机挑选一个整数
d = random.choice(range(10))
print(d)

# 将序列里的所有元素随机排序
list_1 = [1, 1, 2, 3, 4, 5, 6, 7, 8]
list_2 = ["a", "b", "c"]
# random.shuffle(list_1)  # 随机排序
print(list_1)
print("列表元素最大值：", max(list_1))
print("列表元素最小值：", min(list_1))
list_1.append(99)  # 在列表末尾添加新的对象
print(list_1)
print(list_1.count(1))  # 统计某个元素在列表中出现的次数
list_1.extend(list_2)  # 在列表末尾一次性追加另一个序列中的多个值
print("追加另一个序列中的多个值：", list_1)
list_2.insert(1, "h")  # 插入一个对象
print("列表中插入一个对象", list_2)
print("找出某个值第一个匹配项的索引位置:", list_1.index(99))
list_1.pop(1)  # 移除列表中的一个元素
print("移除列表中的一个元素：", list_1)
list_1.reverse()
print("反向列表中的元素:", list_1)
list_2.sort()  # 对原列表进行排序
print("对原列表进行排序:", list_2)
list_2.copy()  # 复制列表
print("复制列表：", list_2)
list_2.clear()  # 清空列表
print("清空列表：", list_2)

# \t 横向制表符
para_str = """这是一个多行字符串的实例，
多行字符串可以使用制表符
TAB（\t）。
也可以使用换行符[\n]
"""
print(para_str)

# 检测字符串中是否包含了子字符串
a_a = "123456789"
b_b = a_a.index("3", 0, len(a_a))
c_c = "Asd"
d_d = "QWER"
print("b_b=", b_b)
print("如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False：", a_a.isalnum())
print("如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False:", a_a.isalpha())
print("如果字符串只包含数字则返回 True 否则返回 False..:", a_a.isdigit())
print("如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False:", c_c.islower())
print("如果字符串中只包含数字字符，则返回 True，否则返回 False:", a_a.isnumeric())
print("如果字符串中只包含空白，则返回 True，否则返回 False.:", c_c.isspace())
print("如果字符串是标题化的(见 title())则返回 True，否则返回 False:", a_a.istitle())
print("如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False：", c_c.isupper())
print(c_c.join(d_d))  # 以指定字符串作为分隔符，将 c_c 中所有的元素(的字符串表示)合并为一个新的字符串
print(c_c.lower())  # 转换字符串中所有大写字符为小写.
print("a_a字符串长度：", len(a_a))
print("返回字符串中最大的字母：", max(d_d))
print("返回字符串中最小的字母：", min(d_d))
