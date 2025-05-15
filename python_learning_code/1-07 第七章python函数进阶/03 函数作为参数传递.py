# 函数作为参数传递
def test_func(compute):
    result = compute(1,2) # 运行compute逻辑 不一定是固定的外部函数
    print(result)
def compute(x,y):
    return x+y
def sub(x,y):
    return x-y
test_func(compute)# 传递的是一种计算逻辑 而不是数据的传递 任何计算逻辑均可以传入
test_func(sub)


# def test_func(a,b):
#     result = compute(a,b)
#     print(result)
# def compute(x,y):  # 函数嵌套调用 只能用固定的compute
#     return x+y

