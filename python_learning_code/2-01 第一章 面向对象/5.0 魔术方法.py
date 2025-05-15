# 常用类内置方法 包括__init__ 也称为魔术方法
# __str__ __lt__ __le__ __eq__ 有二三十个魔术方法


class stu :
    def __init__(self,name,age,addr):
        self.name = name
        self.age = age
        self.addr = addr

    # print 类对象时候 打印的是内存地址 可以通过__str__方法 控制类转字符串行为
    def __str__(self):
        return f"student类对象:,name:{self.name},{self.age},{self.addr}"


    # __lt__ 小于符号比较 直接进行2个类对象的比较是不可以的 需要用到__lt__
    def __lt__(self,other):
        return self.age < other.age # 两个对象进行<比较时候, 自动调用

    # __le__ # 小于等于运算符
    def __le__(self,other):
        return self.age <= other.age

    # __eq__ 比较运算符
    def __eq__(self,other):
        return self.age == other.age


student = stu("周绝伦",22,"woc核武器")
student2 = stu("linjunjie",21,"wocshenre")
print(student <= student2) # 调用了 le方法
print(student < student2)
print(student != student2)

#
