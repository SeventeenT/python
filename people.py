# 定义类
class people:
    # 定义基本属性
    name = ""
    age = 0
    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s说：我%d岁" % (self.name, self.age))


# 实例化类
p = people("Tom", 10, 30)
p.speak()


# 单继承示例
class Child(people):
    grade = ""

    def __init__(self, n, a, w, g):
        # 调用父类的构造函数
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s说：我%d岁了，我在读%d年级" % (self.name, self.age, self.grade))


c = Child("Ken", 10, 60, 3)
c.speak()


# 另一个类，多重继承之前的准备
class Speaker():
    topic = ""
    name = ""

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫%s，我是一个演说家，我演讲的主题是%s" % (self.name, self.topic))


# 多重继承
class Sample(Speaker, Child):
    a = ""

    def __init__(self, n, a, w, g, t):
        Child.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)

    # def speak(self):
    #     print("子类重写父类方法")

    # 类的私有方法
    def __s(self):
        print("  1111 ")


test = Sample("Tim", 10, 60, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法


# 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector(%d,%d)" % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)


class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 如果没有重载函数的话输出的就是一串看不懂的字符串：
    def __str__(self):
        return '这个人的名字是%s,已经有%d岁了！' % (self.name, self.age)


a = people('孙悟空', 999)
print(a)
