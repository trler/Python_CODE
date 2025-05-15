# 如何用程序描述显示?
# 完事万物无非 事情 物体; 而二者都有 属性 和 行为


# 对象和类 让对象干活
class Clock:
    id = None
    price = None
    def ring(self):
        import winsound
        winsound.Beep(100, 100)

clock1 = Clock()
clock1.id = "01000"
clock1.price = 19.00
print(f":脑子id:{clock1.id},价格:{clock1.price}")
clock1.ring()

# 什么是面向对象编程 设计一个类,创建一个对象,使用对象编程



