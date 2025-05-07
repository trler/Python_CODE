# 自定义工具包
# 包内两个模块,str_util.py 字符串相关工具,
    # str_resverse(s), 反转字符串返回
    # substr(s,x,y),按照下标x,y将字符串切片
import my_package1
from my_package1 import *

# 文件操作模块, file_util.py
    # print_file_info(file.name) 接受传入文件路径,打印文件全部内容,如果文件不存在则捕获异常,输出提示信息,通过finally关闭文件对象
    # append_to_file(file.name,data),接受文件路径传入数据,将数据追加到文件中
# from my_package1 import*
print(my_package1.str_util.sub_str("和人阿斯蒂芬阿斯蒂芬",2,5))
print(my_package1.str_util.str_reverse("神人来饿了"))

file_util.print_file_info("test.txt")
file_util.append_to_file("a1.txt","化身恶魔了")
file_util.print_file_info("a1.txt")

print(str_util.sub_str("和人阿斯蒂芬阿斯蒂芬",2,5))
print(str_util.str_reverse("神人来饿了"))