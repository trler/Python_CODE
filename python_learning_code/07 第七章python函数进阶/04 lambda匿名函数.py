# def关键字 是定义带有名称的函数
# lambda关键字定义 定义匿名函数 无名称
# 匿名函数只能临时使用依次

# lambda 传入参数:函数体(一行代码无法写多行)

def test_func(compute):
    result = compute(1,2)
    print(f"result={result}")
def compute(x,y):
    return x+y
test_func(compute)

def test_func(compute):
    result = compute(1,2)
    print(f"result={result}")
test_func(lambda x,y:x+y) # 把函数表达式直接写入参数 节省空间代码 类似临时变量



