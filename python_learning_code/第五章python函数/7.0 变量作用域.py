# ·使用global关键字可以在函数内部声明变量为全局变量
num = 100
def test_a():
    print(f"test_a: {num}")
def test_b():
    global num
    num = 2

    print(num)
test_a()
test_b()
# 1.什么是局部变量
# 作用范围在函数内部,在函数外部无法使用
# 2.什么是全局变量
# 在函数内部和外部均可使用
# 3.如何将函数内定义的变量声明为全局变量
# 使用global关键字,global变量