# 循环语句
n = 100
sun = 0
counter = 1
while counter <= n:
    sun = sun + counter
    counter += 1
print("1 到 %d 之和为：%d" % (n, sun))

print("=" * 30)

# while...else 循环使用
count = 0
while count < 5:
    print(count, "小于5")
    count = count + 1
else:
    print(count, "大于或等于5")

# 类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中 (写在同一行会提示)
# flag = 1
# while flag:
#     print("欢迎访问菜鸟教程！")

print("=" * 30)

# for 语句
sites = ["baidu", "google", "runoob", "taobao"]
for site in sites:
    if site == "runoob":
        print("菜鸟教程！")
        break
else:
    print("没有循环数据")
print("完成循环！")

# 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
for i in range(5):
    print(i)
# 可以使用range指定区间的值
for i in range(1, 10):
    print("区间值：", i)
# 可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长')
for i in range(0, 10, 3):
    print("指定增量：", i)
# 负数
for i in range(-10, -100, -30):
    print(i)

print("=" * 30)

# 结合range()和len()函数以遍历一个序列的索引
t = ["Google", "Baidu", "Runoob", "Taobao", "QQ"]
for i in range(len(t)):
    print(i, t[i])

a = list(range(5))
print("用range()函数创建列表：", a)

print("=" * 30)

# break和continue语句及循环中的else子句
# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
for letter in "Runoob":
    if letter == "o":
        break
    print("当前字母为：", letter)

print("=" * 30)

var = 10
while var > 0:
    print("当前变量值为：", var)
    var = var - 1
    if var == 5:
        break

print("=" * 30)

# continue 语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
for letter in "Runoob":
    if letter == "o":
        continue
    print("当前字母为：", letter)

var1 = 10
while var1 > 0:
    var1 = var1 - 1
    if var1 == 5:
        continue
    print("当前变量值为：", var1)

print("=" * 30)

# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "等于", x, "*", n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, "是质数")

print("=" * 30)

# Python pass是空语句，是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句
for b in "Runoob":
    if b == "o":
        pass
        print("执行pass块")
    print("当前字母：", b)

