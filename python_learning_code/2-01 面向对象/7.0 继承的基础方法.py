# 概念
# 一个旧手机phone 现在要创建一个型手机 phone2025 如何设计, 从头到位设计,还是基于老的类进行修补
# 把已有的东西拿过来,


# 使用方法
class phone:
    IMEI = 'IMEI'
    producer = 'producer'

    def call_by_4g(self):
        print("4g童话")

# 单继承
class phone2025(phone): # class 类名(父类名) 单继承
    face_id = True
    def call_by_5g(self):
        print("5g童话")

# hp = phone2025()
# hp.call_by_4g()

# 多继承 继承多个父类
class   NFCreader:
    NFC_type = "第五代"
    producer = "HW"

    def read_card(self):
        print("NFC读卡")
    def write_card(self):
        print("NFC写卡")

class   remotecontrol :
    re_type = "红外遥控"
class xiaomi_phone(phone2025,remotecontrol,NFCreader)   :
    re_type = "紫外遥控"
    pass

# pass 关键字

ph = xiaomi_phone()
ph.call_by_4g()

# 调用同名成员属性时候 谁先来的谁的优先级高