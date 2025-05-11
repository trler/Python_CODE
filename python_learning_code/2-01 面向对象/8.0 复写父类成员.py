# 复写 子类继承时候 对父类的属性和方法进行改写
# 重新定义方法即可
class phone:
    imei = None
    producer = "itcast"
    def call_by_4g(self):
        print("父类的4g")

class my_phone(phone) :
    producer = "it和解码"  # 复写属性
    def call_by_4g(self):
        print("子类的4g") # 复写方法
        print("6g"
              "haod4g")
        print(f"{phone.producer}<UNK>") # 方法1 直接调用属性
        phone.call_by_4g(self)  # 方法1 直接调用方法
        # print(f"{self.imei}<UNK>")
        print(f"子类中父类为:{super().producer}") # super().父类方法使用
        super().call_by_4g() # super.()调用父类方法
phone1 = my_phone()
phone1.call_by_4g()
print(phone1.producer)

# 调用父类的同名成员 就是想使用父类的原本的成员 两个方式
# 父类.成员变量,方法(self)
# super().成员,方法
print(phone.producer)






