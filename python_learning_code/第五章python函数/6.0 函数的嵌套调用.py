# 1.掌握函数的嵌套调用
# 2.理解嵌套调用的执行流程
def func_a():
    print("---1---")
def func_b():
    func_a()
    print("---2---")
def func_c():
    func_b()
    print("---3---")
func_c()