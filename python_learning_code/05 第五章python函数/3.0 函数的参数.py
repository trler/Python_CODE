# 可以接受外部参数的调用
# def add(x,y):
#     result = x + y
#     print(f"{x} + {y} = {result}")
# add(int(input("输入第一个数字")),int(input("输入第二个数字")))

# 函数定义中,提供的x和y,称之为:形式参数(形参),表示函数声明将要使用2个参数参数之间使用逗号进行分隔
# 函数调用中,提供的5和6,称之为:实际参数(实参),表表示函数执行时真正使用的参数值

def check_hesuan(data):
    if data<=37.5:
        print(f"您的体温为: {data}度,体温正常请进!")
    else:
        print(f"您的体温为: {data}度,体温异常,即将处死!")
check_hesuan(int(input("请输入你的提问")))