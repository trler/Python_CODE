# 每个 Python 文件都可以作为一个模块，模块的名字就是文件的名字。也就是说自定义模块名必须要符合标识符命名规则
# import my_moudle1
# my_moudle1.test(1,2)
#
# from my_moudle1 import *
#
# test(1,2)

# 如果两个模块里面有同名的功能,那么后面的会直接覆盖
# from my_moudle2 import *
# test(1,2)

# 测试模块
import my_moudle1 # 直接运行了模块1中的调用 测试留下的
# 用main变量 from 的时候, 内置变量不相等 看mounddle1 的情况

# _all_变量 from xxx import * 时 只使用_all_里面的元素
from my_moudle1 import *
test(1,2)
from my_moudle1 import test2
test2(1,2)




