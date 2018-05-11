# 判断是不是质数
num = int(input("请输入一个数字：\n"))
# 质数大于1
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("%d 不是质数" % num)
            print(i, "*", num // i, "=", num)
            break
    else:
        print("%d 是质数" % num)
else:
    print("%d 不是质数" % num)

# 输出指定范围内的素数（质数）
lower = int(input("请输入区间最小值：\n"))
upper = int(input("请输入区间最大值：\n"))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}x{}={}\t".format(i, j, i * j), end="")
    print()
