# 1.掌握元组的定义格式
# 2.掌握元组的特点
# 3.掌握元组的常见操作
# 和列表相比,元组一旦形成,就不可以修改,需要在程序内封装数据,有不希望封装的数据被篡改
# 元组定义:定义元组使用小括号,且使用逗号隔开各个数据,,数据可以是不同的数据类型。
#定义元组字面量 (元素,元素,........元素)
#定义元组变量   变量名称=(元素,元素,..........元素)
#定义空元组
#方式1   变量名称=()
#方式2   变量名称=tuple()

# tuple1 = (1,"hello",True)
# t2 = ()
# t3 = tuple()
# print(tuple)
# print(t2)
# print(t3)
# print(f"tuple1的类型是{type(tuple1)},t2的类型是{type(t2)},t3的类型是{type(t3)}")
# # 如果元组只有一个数据,这个数据后要加逗号
# t4 = (1,)# 否则变成表达式了
# # 元组也可以嵌套
# t5 = ((1,2,3),2)
# print(f"t5的类型是{type(t5)}")
#
# # 可以通过下标索引来取出内容
# num = t5[0][1]
# print(num)
#
# # 三个方法 index len元素个数 count统计
# t6 = ("黑马程序员","船只叫用户","python")
# index = t6.index("python")
# print(f"python的下表为{index}")
# count = t6.count("python")
# print(f"python的个数为{count}")
# num1 = len(t6)
# print(f"t6元素个数{num1}")
#
# # 元组遍历 while for
# index = 0
# while index< len(t6):
#     print(t6[index])
#     index += 1
# for item in t6:
#     print(item)
#
# # 可以修改元组中嵌套的list元素
#
# t7 = ([1,2,3],5,6,7)
# print(f"t7是{t7}")
# t7[0][1] = 9999
# print(f"t7修改后变成{t7}") # 确实可以修改

# 练习,元组基本操作 定义一个元组,内容是:('周杰轮',11,['football','music'),记录的是一个学生的信息(姓龄、爱好)
# 请通过元组的功能(方法),对其进行
# 1.查询其年龄所在的下标位置
# 2.查询学生的姓名
# 3.删除学生爱好中的football
# 4.增加爱好:coding到爱好list内

t1 = ('周杰轮',11,['football','music'])
index = t1.index(11)
name = t1[0]
del t1[2][1]
t1[2].append("coding")

print(f"年龄11岁在的下标位置为{index},名字是{name},修改后的元组为{t1}")


