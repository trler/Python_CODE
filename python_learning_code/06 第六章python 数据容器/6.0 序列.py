# 1.了解什么是序列
# 2.掌握序列的切片操作
from idlelib.debugobj import myrepr
from idlelib.run import MyHandler

# 序列是指:内容连续、有序,可使用下标索引的一类数据容器
# 列表、元组、字符串,均可以视为序列。

# 序列支持切片,即:列表、元组、字符串,均支持进行切片操作
# 切片:从一个序列中,取出一个子序列
# 语法:序列[起始下标:结束下标:步长]

# 表示从序列中,从指定位置开始,依次取出元素,到指定位置结束,得到一个新序列:
# 起始下标表示从何处开始可以留空,留空视作从头开始
# 结束下标(不含)表示何处结束,可以留空,留空视作截取到结尾
# 步长表示,依次取元素的间隔
# 步长1表示,一个个取元素
# 步长2表示,每次跳过1个元素取
# 步长N表示,每次跳过N-1个元素取
# 步长为负数表示,反向取(注意,起始下标和结束下标也要反向标记)

my_list = [0,1,2,3,4,5,6]
result1 = my_list[1:4]
print(f"原列表{my_list},按要求变换后列表{result1}")

my_tuple = (0,1,2,3,4,5,6)
result2 = my_tuple[:]
print(f"原元组{my_tuple},按要求切片后元组{result2}")

my_str = ("itheima and itcast")
result3 = my_str[::2]
print(f"原字符串{my_str},按要求变换后{result3}")
result4 = my_str[::-1]# 反转
print(f"原字符串{my_str},变换后{result4}")

result5 = my_list[3:1:-1]
print(f"原列表{my_list},变换后{result5}")

result6 = my_tuple[::-2]
print(f"变换后{my_tuple},变换后{result6}")

# 作业 有字符串:"万过薪月,员序程马黑来,nohtyP学"
# 请使用学过的任何方式,得到"黑马程序员"
# 可用方式参考:
# 倒序字符串,切片取出或切片取出,然后倒序
# split分隔","replace替换"来"为空,倒序字符串

my_str = "万过薪月,员序程马黑来,nohtyP学"
result7 = my_str[::-1][9:14]
result8 = my_str[5:10][::-1]
print(f"{result8}")
# result7 = result7[9:14]
print(f"{result7}")
# list = my_str.replace("来"," ")
# list2 = list.split(",")
# print(f"{list2}")
# list3 = list2[1][::-1].strip(' ')
# print(f"{list3}")

list = my_str.replace("来"," ").split(",")[1].strip(' ')[::-1]#??? 链式调用
print(f"{list}")



