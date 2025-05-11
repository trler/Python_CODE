# 形参注解
# def func(data): # 本意传入list
#     data.app # 但是无提示
# func() # 提示框不提示传入参数类型
def add(x:int ,y: int) -> int  :# 对形参,返回值类型 进行注释
    return x+y
def func(data:list):
    return data # 有了自动补全
add(x=1, y=2) # 有了要输入参数类型提示
print(func(1)) # 提示性 不影响函数





# 返回值注解