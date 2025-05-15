# 构造方法 向成员变量赋值
# python类 可以使用 __init__()方法 称之为 构造方法
# 构建类对象时候 会自动执行,且会将传入参数,自动传递给__init__方法使用
import sys


class student:
    name = None # 属性可以省略 直接下面声明＋赋值
    age = None
    tel = None

    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("student类创建了一个对象")
stu = student(name='蛤目的哈贝贝',age=22,tel="11454156651")
print(stu.name)
print(stu.age)
print(stu.tel)


# 案例 学生信息录入

class stu_info_load :

    # def __init__(self,name=input("请输入学生姓名"),age=input("请输入学生年龄"),addr=input("请输入学生地址")):
    #     self.name = name
    #     self.age = age
    #     self.addr = addr
    #     print(f"学生信息录入成功,信息为:[学生姓名:{self.name}, 年龄:{self.age}, 地址:{self.addr}]")

    # 错误的, 类对象未创建 即赋值

    def __init__(self):
        self.name = input("请输入学生姓名")
        self.age = age=input("请输入学生年龄")
        self.addr = addr=input("请输入学生地址")
        print(f"学生信息录入成功,信息为:[学生姓名:{self.name}, 年龄:{self.age}, 地址:{self.addr}]")
stu_info = []
for i in range(0,10):
    print(f"当前输入第{i+1}位学生信息,总共需要输入10位学生信息")
    stu_info.append(stu_info_load())
num = 1
for i in stu_info:
    print(f"第{num}个人的名字是:{i.name},<UNK>:{i.age},<UNK>:{i.addr}")
    num += 1





