# 列表的定义
# 字符串变量存储一个人的名字,列表存储多个人的名字
# 基本语法:
# #字面量
# [元素1,元素2,元素3,元素4,....]
# #定义变量
# 变量名称[元素1,元素2,元素3,元素4,....]
# #定义空列表
# 变量名称= []
# 变量名称= list()

# 可以支持不同数据类型 甚至支持嵌套
# name_list =  ['1li','阿斯蒂芬','阿斯弗']
# my_list = [1, 'itheima', True,name_list]
# list2 = [1,2,3,4,[1,2,[123,32]]]
# print(my_list)
# print(type(my_list))# 数组?
# print(list2)

# 下标索引
# 如何从列表中取出特定位置的数据呢 同数组一样
# print(list2[4])
# 反向索引 从-1开始从右往左数
# print(list2[-1][2][-2])0

# list 常用操作 掌握列表的常用操作方法
# 插入,删除,清空,修改,统计元素个数 统称为列表的方法
# 回忆:函数是一个封装的代码单元,可以提供特定功能。
# 在Python中,如果将函数定义为class(类)的成员,那么函数会称之为:方法
#
# class student:
#     def add(self,x,y):
#         return x+y
# 方法和函数功能一样,有传入参数,有返回值,只是方法的的使用格式不同
#
# 函数的使用:num = add(1, 2)
# 方法的使用:
# student = Student()
# num = student.add(1, 2)

# list.把方法点出来

# 1. 查询某元素的下表,如果找不到报错ValueError
# list.index('itheima')语法

# my_list = [1, 2, 3,"itheima"]
# num=my_list.index('itheima')
# print(num)# 返回itheima的下标位置

# 2,修改特定位置的元素值
# my_list = [1, 2, 3,"itheima"]
# my_list[2] = "shenren"
# print(my_list)#

#3,在指定下标,插入元素
# 语法:list.insert(下表,索引),在指定下标,插入元素
# my_list = [1, 2, 3,"itheima"]
# my_list.insert(1,"神人")
# print(my_list)

#4,追加元素,添加到最后列表的尾部
# my_list = [1, 2, 3,"itheima"]
# my_list.append("神人")
# print(my_list)#

# 5,追加元素2,
# list.extend(其他数据容器),将数据容器拼接到list的后面
# my_list = [1, 2, 3,"itheima"]
# my_list2 = ["神人","狗","飞起来"]
# my_list.extend(my_list2)
# print(my_list)

# 6,删除元素
# 语法1,del list[下标]
# 语法2,list.pop<下标>
# my_list = [1, 2, 3,"itheima"]
# del my_list[3]
# print(my_list)#
# ret = my_list.pop(1) # 取出后返回
# print(my_list)
# print(ret)

# 7,指定一个元素删除列表中的第一个匹配项
# my_list = [1, 2, 3,"itheima",3]
# my_list.remove(3)
# print(my_list)#

# 8,清空列表
# my_list = [1, 2, 3,"itheima",3]
# my_list.clear()
# print(my_list)# 空列表

# 9,统计元素在列表中的个数
# my_list = [1, 2, 3,"itheima",3]
# num = my_list.count(3)
# print(num)#

# 10,统计列表元素个数
# my_list = [1, 2, 3,"itheima",3]
# num = len(my_list)
# print(num)#

#作业 常用功能
my_list = [21,25,21,23,22,20]
my_list.append(31)
my_list2 = [29,33,30]
my_list.extend(my_list2)
first = my_list[0]
end = my_list[-1]
print(f"第一个元素是{first}, 最后一个元素是{end}")
num = my_list.index(31)
print(f"31的索引是{num}")



























