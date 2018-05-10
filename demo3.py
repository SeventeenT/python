# 判断闰年
year = int(input("请输入一个年份：\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("%d年是闰年" % year)
        else:
            print("%d年不是闰年" % year)
    else:
        print("%d年是闰年" % year)
else:
    print("%d年不是闰年" % year)

# 合并写法
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("%d年是闰年" % year)
else:
    print("%d年不是闰年" % year)

# 获取最大值函数
print(max(1, 2))
print(max("a", "b", "c"))
print(max([1, 3, 5, 7]))
print("80, 100, 1000 最大值为: ", max(80, 100, 1000))
print("[0, 100, -400]最大值为: ", max([0, 100, -400]))

# 对比任意多个数字大小
N = int(input("输入需要对比大小数字的个数："))
num = [int(input("请输入第%d个对比数字\n" % i)) for i in range(1, N + 1)]
print("您输入的数字为：", list(num))
print("最大值为：", max(num))

