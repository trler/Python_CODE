# 1.掌握集合的定义格式
#    集合使用{}
# 2.掌握集合的特点
# 3.掌握集合的常见操作
set_1 = {1,2,3}
set_2 = set([1,2,3])
my_set = {"船只教育","黑马程序员","itheima","船只教育","黑马程序员","itheima","船只教育","黑马程序员","itheima"}
my_set_empty =set()
print(f"{my_set}my_set,={type(my_set)}")
print(f"{my_set_empty},my_set_empty,={type(my_set_empty)}")
# 下表索引无法使用 序列不包含set
# 允许修改内容 修改方法

# 添加 set.add
my_set.add("python")
my_set.add("船只教育")
print(f"my_set添加python和船只教育后变成{my_set}")

# 移除元素 set.remove
my_set.remove("黑马程序员")
print(f"my_set移除黑马程序员后变成{my_set}")

# 随机取出 set.pop
pop1 = my_set.pop()
print(f"取出元素为pop1={pop1},取出后变成{my_set}")

# 清空集合 clear
my_set.clear()
print(f"清空集合后为{my_set}")# 空集合

# 取两个集合的差集 得到一个新集合,集合1有,2没有 set1.diference(set2)
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"set1={set1},set2={set2},set3={set3}")

# 消除2个集合的差集 set1.difference_update(set2) 在集合1内消去与集合2相同的元素 集合1被修改,2不变
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)
print(f"set1={set1},set2={set2}")

# 集合合并 set1.union(set2)
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(f"set1={set1},set2={set2},set3={set3}")

# 统计元素数量 .len
set1 = {1,2,3,1,2,3,3,2,2}
print(f"set1={set1},len(set1)={len(set1)}")

# 集合的遍历 不能用while 不支持下表索引 可以用for
set1 = {1,2,3,1,2,3,3,2,2}
for element in set1:
    print(f"集合元素有{element}")

# 作业 信息去除
# 有如下列表对象my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
# 定义一个空集合
# for循环遍历连表
# 在for循环中将列表的元素添加到集合
# 将最终得元素去重后的集合打印

my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
my_set = set()
i = 1
for element in  my_list:
    print(f"列表中第{i}个元素为{element},将其添加到set中")
    my_set.add(element)
    i +=1
print(f"去重后的集合为{my_set}")



