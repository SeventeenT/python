# coding=utf-8
# %% 百分号标记 #就是输出一个%
# %c 字符及其ASCII码
# %s 字符串
# %d 有符号整数(十进制)
# %u 无符号整数(十进制)
# %o 无符号整数(八进制)
# %x 无符号整数(十六进制)
# %X 无符号整数(十六进制大写字符)
# %e 浮点数字(科学计数法)
# %E 浮点数字(科学计数法，用E代替e)
# %f 浮点数字(用小数点符号)
# %g 浮点数字(根据值的大小采用%e或%f)
# %G 浮点数字(类似于%g)
# %p 指针(用十六进制打印值的内存地址)
# %n 存储输出字符的数量放进参数列表的下一个变量中


name = "Zed A. Shaw"
age = 35  # not a lie
height = 74
weight = 180
eyes = 'Blue'
teeth = 'white'
hair = 'Brown'

height_conversion = 2.54
weight_conversion = 0.4535924

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teech are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d,%d and %d I get %d." % (age, height, weight, age + height + weight)

print "He's %.2fcm height." % (height * height_conversion)
print "He's %.3fkg weight." % (weight * weight_conversion)

# 四舍五入
r1 = round(3.57777)
r2 = round(2.2323)
print "r1 = %s, r2 = %s" % (r1, r2)
