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
