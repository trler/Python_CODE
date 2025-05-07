# 模块的导入
    # 什么是模块
    # module 就是一个py文件,里面有各种各样的类,函数变量,可以直接拿过来用

    # 导入python内置模块 time
# import time # 导入python内置的time模块
# print("1")
# time.sleep(1) # 通过. 就可以使用模块内部的全部功能,(类,函数,变量)
# print("2")
# time.sleep(2)
# print("3")
#
    # form 关键字实现导入  from 模块名 import 功能名 引入具体的某个功能 sleep
# from time import sleep
# print("你好")
# sleep(5)
# print("我熬")

    # from  模块名 import* 全部的意思
# from time import *
# sleep(5) # 不需用写个time.

    # as 定义别名 import 模块名 as 别名  form..
# import time as t
# t.sleep(1)
from time import sleep as sl
sl(34)








