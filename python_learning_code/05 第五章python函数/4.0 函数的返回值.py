
# 1.掌握函数返回值的作用
# 2.掌握函数返回值的定义语法
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
r = add(5.6,6)
print(r)
# 1.什么是函数返回值?
# 函数在执行完成后,返回给调用者的结果
# 2.返回值的应用语法:
# 使用关键字:return来返回结果
# 3.注意
# 函数体在遇到return后就结束了,所以写在return后的代码不会执行。

# None类型
# 如果函数没有使用return来返回语句,那么函数还会有返回值吗
# 实际上是:有的。
# Python中有一个特殊的字面量:None,其类型是:<class'NoneType>
# 无返回值的函数,实际上就是返回了:None这个字面量
def say_hello():
    print("hello")
num = say_hello()
print(type(num))

def check_age(age):
    if age >= 18:
        return "success"
    else:
        return None

result = check_age(16)
if result is None:
    print("未满足十八")
# 用于声明无内容的变量上
# ·定义变量, 但暂时不需要变量有具体值, 可以用None    来代替
# 斩不赋予变量目休值