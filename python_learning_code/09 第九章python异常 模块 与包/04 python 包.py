# 自定义包
    # 什么是python包
    # python包就是一个文件夹,文件夹包含了一个__init__.py文件,里面有多个模块文件 Package包
    # 逻辑上看,包的本质依然是模块
    # 模块文件越来越多时,包可以帮助我们管理这些模块

    # 如何自定义包
    # pycharm 右键自定义包
# import my_package.my_module1
# import my_package.my_module2
#
# my_package.my_module1.info_print1()
# my_package.my_module2.info_print2()

    # from 语句导入
# from my_package import my_module1
#
# from my_package.my_module1 import info_print1
# info_print1()

    # __all__ import *的功能
from my_package import *
my_module1.info_print1()
# my_module1.info_print2()



# 第三方包
    # 什么是第三方包
    # pip安装
    # pycharm
import numpy.random as rnd

