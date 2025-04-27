# 1,基础用法
# while循环条件自定义,自行控制循环条件
# for循环是轮询机制

# name = "itheima"
# for x in name:# 将name中的内容,挨个取出赋予x临时变量
#                 #可以在循环体内对x进行处理
#     print(x)
# 可以看出，for 循环是将字符串的内容：依次取出
# 所以，for 循环也被称之为：遍历循环

# 同 while 循环不同，for 循环是无法定义循环条件的。
# 只能从被处理的数据集中，依次取出内容进行处理。
# 所以，理论上讲，Python 的 for 循环无法构建无限循环 (被处理的的数据集不可能无限大)

# 练习

# name1 = "itheima is a brand of itcast"
# num =  0
# for x in name1:
#     if x == "a":
#         num +=1
# print(f"{name1}中有{num}个a")


#  range 语句

# 语法中的:待处理数据集,严格来说,称之为:序列类型
# 序列类型指,其内容可以一个个依次取出的一种类型,包括:字符串,元组,什么的

# 语法1  range (num)
# 获取一个从 0 开始，到 num 结束的数字序列 (不含 num 本身)
# 如 range (5) 取得的数据是:[0,1,2,3,4]
# 语法2:
# range(num1, num2)
# 获得一个从num1开始,到num2结束的数字序列(不含num2本身)
# 如,range(5,10)取得的数据是:[5,6,7,8,9]
# 语法3:
# range(num1, num2, step)
# 获得一个从num1开始,到num2结束的数字序列(不含num2:本身)
# 数字之间的步长,以step为准(step默认为1)
# 如,range(5,10,2)取得的数据是:[5,7,9]

# for x in range(10) :
#     print(x)

# for x in range(4,13):
#     print(x)

# for x in range(400,10000, 400):
#     print(x)

# i = 1;
# while i <= 10:
#     print("送花")
#     i += 1
# for x in range(10):
#     print("送花")

# 练习 有几个偶数
# num = int(input("输入想要的上限制:"))
# count = 0
# for x in range(1,num+1):
#     if x%2 == 0:
#         count += 1
# print(f"从1到{num}中一共有{count}个偶数")


# 变量作用域

