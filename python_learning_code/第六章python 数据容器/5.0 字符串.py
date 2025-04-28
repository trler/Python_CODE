# 字符串的常见操作
# 字符串是字符的容器,一个字符串可以存放任意数量的字符。
# 如,字符串:"itheima"
from operator import index

my_str = "itheima and itcast"

# 通过下标索引取值
value1 = my_str[2]
value2 = my_str[-1]
print(f"{value1},{value2}")

# 字符串同元组一样,无法修改

# index 方法 查找特定字符串的索引值
value = my_str.index("and")
print(f"在字符串{my_str}查找and,下标记为{value}")

# replace方法 学符串的替换
# 语法:字符串.replace(字符串1,字符串2)
# 功能:将字符串内的全部:字符串1替换为字符串2
# 注意:不是修改字符串本身,而是得到了一个新字符串哦
new_my_str  = my_str.replace("it","神人")
print(f"将字符串{my_str}替换后变成{new_my_str}")

# split 字符串分割
# 语法:字符串.split(分隔符字符串)
# 功能:按照指定的分隔符字符串,将字符串划分为多个字符串,并存列表对象中
# 注意:字符串本身不变,而是得到了一个列表对象

my_str = ("hello python itheima itcast")
my_str_list = my_str.split(" ")
print(f"将字符串{my_str},进行split切分后变成{my_str_list}")

# strip 方法,字符串规整,去除前后空格 如果输入字符,则去除头尾的对应字符串
my_str = "  itheima and itcast "
new_my_str = my_str.strip()
print(f"{my_str}变成{new_my_str}")

my_str = ("12itheima and itcast21")
new_my_str = my_str.strip("12")
print(f"{my_str}{new_my_str}")

# 统计字符串出现次数 count
my_str= "hello itheima hello itcast hello"
num = my_str.count("he")
print(f"he出现了{num}次,在{my_str}")

# len统计字符串长度
num = len(my_str)
print(f"字符串{my_str},长度是{num}")

# 同样支持 for while 循环遍历
my_str=("黑马人")
index = 0
while index < len(my_str):
    print(my_str[index])
    index += 1
for i in  my_str:
    print(i)

# 作业 给定字符串 "itheima itcast boxuegu"
# 统计有多少it 字符 , 将字符串空格 全部替换成| ,按照|进行字符串分割,得到列表
my_str = "itheima itcast boxuequ"
num = my_str.count("it")
my_str2 = my_str.replace(" ","|")
my_str2_list = my_str2.split("|")
print(f"原本字符串为{my_str}有{num}个it字符,将空格替换成|后变成"
      f"{my_str2},按照|分割后变成{my_str2_list}")


