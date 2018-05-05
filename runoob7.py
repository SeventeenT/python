import sys  # 引入sys模块

# 迭代器与生成器
# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
a = [1, 2, 3, 4]
it = iter(a)  # 创建迭代器对象
# print("1", next(it))
# print("2", next(it))
# 使用for语句遍历
for x in it:
    print(x, end=" ")

print("\n", "=" * 30)

b = [1, 2, 3, 4]
it_b = iter(b)
i = 0
while i < len(b):
    try:
        print(next(it_b))
        i += 1
    except StopIteration:
        break
#         sys.exit(0)  # 执行该句程序会直接退出，后面的程序将不再执行

print("=" * 30)


# 生成器

def fibonacci(n):  # 生成器函数
    k, l, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield k
        k, l = l, k + l
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        break
