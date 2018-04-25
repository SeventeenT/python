# coding=utf-8
# 定义x的变量
x = "There are %d types of people." % 10
# 定义binary变量
binary = "binary"
# 定义do_not变量
do_not = "don't"
# 格式化字符  定义y
y = "Those who know %s and those who %s." % (binary, do_not)
print(x)
print(y)

# %r和%s的区别
# %r  用来做  debug  比较好，因为它会显示变量的原始数据（ raw data ），而其它的符号则是用来向用户显示输出的。
print("I said: %r." % x)
print("I said: %s." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print (joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)