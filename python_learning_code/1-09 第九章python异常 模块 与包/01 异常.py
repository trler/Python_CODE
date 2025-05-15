# 检测到错误 bug 就是异常

# 异常捕获方式
# 1,bug停止运行
# 2,bug进行提醒,整个程序可以继续运行
# 捕获异常的作用在于:提前假设某处会出现异常,做好提是前准备,当真的出现异常的时候,可以有后续手段。
    # try(可能错误代码)
    # except(出现异常执行的代码)

# 基本捕获语法
# try:
#     f = open('file.txt', 'r', encoding='utf-8')
# except:
#     print('出现异常,文件不存在')
#     f = open('file.txt', 'w', encoding='utf-8')

# 捕获指定异常
# try:
#     print(name)
# except NameError as e:
#     print("出现了变量未定义异常")
#     print(e)

# 捕获多个异常
# try:
#     print(name)
#     1/0
# except (NameError, ZeroDivisionError) as e: # 写进元组 # 未定义异常类型,将无法捕获
#     print("")

# 捕获全部异常 except 后面什么也不写
# try:
#     1/0
# except Exception as e: print(e)

# 异常else else表示的是如果没有异常时候,应该怎么做
# try:
#     f = open("test.txt","r")
#     print("ok?")
# except:
#     print("笑了")
#     f = open("test.txt","w")
# else:
#     print("没出现异常")
# finally:
#     print("此时的我已然开始摆烂")
#     f.close()

# 异常的传递性
# 内层函数的异常可以被外层函数捕获,如果一直未被捕获,会报错
def func1():
    print("func1 开始执行")
    num = 1/0
    print("func1 结束执行")
def func2():
    print("func2 开始执行")
    func1()
    print("func2 结束执行")

def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了 可能是:{e}")
main()
