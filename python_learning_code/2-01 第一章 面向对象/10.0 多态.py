# 多态
# 多态指的是 多种状态 完成某个行为时候, 使用不同的对象会得到不同的状态
# 函数(方法)形参声明接收父类对象
# 实际传入父类的子类对象进行工作
from jinja2.filters import do_groupby


# 父类做定义声明
# 子类做实际工作
# 获得同一行为,不同状态
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print('Dog is speaking')
class Cat(Animal):

    def speak(self):
        print('Cat is speaking')


def make_noise(animal: Animal):
    animal.speak()
dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)



# 抽象类(接口)编程思想
# Animal 的speak方法 是空实现 父类来确定有那些方法 由子类去实现它 这种写法叫做抽象类, 也叫接口
# 抽象方法: 方法体为pass的就是抽象方法 有抽象方法的类叫抽象类

# 抽象类好比定义一个标准,包含了一些抽象的方法, 要求子类必须实现

class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_wind(self):
        pass
class midea_AC(AC):
    def cool_wind(self):
        print('meidi cool wind')
    def hot_wind(self):
        print('meidi hot wind')
    def swing_wind(self):
        print('meidi swing wind')
class xiaomi_AC(AC):
    def cool_wind(self):
        print('ge cool wind')
    def hot_wind(self):
        print('ge hot wind')
    def swing_wind(self):
        print('ge swing wind')

def make_cool(ac: AC): # 直接定义对象了吗
    ac.cool_wind()

md_ac = midea_AC()
gr_ac = xiaomi_AC()

make_cool(gr_ac)
make_cool(md_ac)

print(type(gr_ac))
print(type(md_ac))