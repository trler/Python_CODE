# 类的定义与使用语法
# class 创建类型:内容体(属性(类中变量),行为(函数)或者成员方法)
# 创建类对象的语法    对象 = 类名称()
    # def 方法名(self,形参1,形参2)
    #     方法体

class Student:
    name = None
    def say_hi(self): # 必须出现self
        print('Hello, my name is %s' % self.name)  # 访问其他成员方法 需要.一下
    def say_hi2(self,msg):
        print(f"大家好,我是:{self.name},{msg}")# 访问外部传入的 msg 不需要self关键字

stu_1 = Student()
stu_1.name = '花木'
stu_1.say_hi()
stu_2 = Student()
stu_2.name = '鬼母'
stu_2.say_hi()
stu_3 = Student()
stu_3.name = 'hamude1'
stu_3.say_hi()

stu_1.say_hi2('哎呦不错呦')
stu_2.say_hi2('此时的我 笑嘻嘻了')
stu_3.say_hi2('蛤目的航母啊')




















