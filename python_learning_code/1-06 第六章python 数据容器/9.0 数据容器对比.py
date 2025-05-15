# 数据容器可以从以下视角进行简单的分类:

# 是否支持下标索引
#   支持:列表、元组、字符串-序列类型
#   不支持:集合、字典-非序列类型

# 是否支持重复元素:
#   支持:列表、元组、字符串-序列类型
#   支持:集合、字典-非序列类型

# 是否可以修改
#   支持:列表、集合、字典
#   不支持:元组、字符串

# 通用操作

# 都支持 for 循环
# while只支持序列循环

# len() max() min() 统计容器元素个数,最大元素,最小元素

my_list = [1,2,23,4,5]
my_tuple = (1,2,233,4,5)
my_str = "abfcdef"
my_set = {1,2,233,4,5}
my_dict = {"key1": 1, "key3": 2, "key2": 3, "key4": 4, "key5": 5}

print(f"列表元素个数有:{len(my_list)}")
print(f"元组元素个数有:{len(my_tuple)}")
print(f"字符串元素个数有:{len(my_str)}")
print(f"集合元素个数有:{len(my_set)}")
print(f"字典元素个数有:{len(my_dict)}")

print(f"列表最大元素个数为:{max(my_list)}")
print(f"元组最大元素个数为:{max(my_tuple)}")
print(f"字符串最大元素个数为:{max(my_str)}") # 如何比大小
print(f"集合最大元素个数为:{max(my_set)}")
print(f"字典最大元素个数为:{max(my_dict)}") # 如何比大小 下视频

print(f"列表最小元素个数为:{min(my_list)}")
print(f"元组最小元素个数为:{min(my_tuple)}")
print(f"字符串最小元素个数为:{min(my_str)}") # 如何比大小
print(f"集合最小元素个数为:{min(my_set)}")
print(f"字典最小元素个数为:{min(my_dict)}") # 如何比大小 下视频

# 类型转换  转列表
print(f"列表转列表的结果是:{list(my_list)}")
print(f"元组转列表的结果是:{list(my_tuple)}")
print(f"字符串转列表的结果是:{list(my_str)}") # 每个元素都取了出来
print(f"set转列表的结果是:{list(my_set)}")
print(f"字典转列表的结果是:{list(my_dict)}") # key值

# 转元组
print(f"列表转 元组的结果是:{tuple(my_list)}")
print(f"元组转 元组的结果是:{tuple(my_tuple)}")
print(f"字符串转元组结果是: {tuple(my_str)}") # 每个元素都取了出来
print(f"set转元组的结果是:  {tuple(my_set)}")
print(f"字典转 元组的结果是:{tuple(my_dict)}") # key值
# 转字符串
print(f"列表转 字符串的结果是:{str(my_list)}")
print(f"元组转 字符串的结果是:{str(my_tuple)}")
print(f"字符串转字符串结果是: {str(my_str)}") # 每个元素都取了出来
print(f"set转字符串的结果是:  {str(my_set)}")
print(f"字典转 字符串的结果是:{str(my_dict)}") # key值

# 转set
print(f"列表转 集合的结果是:{set(my_list)}")
print(f"元组转 集合的结果是:{set(my_tuple)}")
print(f"字符串转集合结果是: {set(my_str)}") # 每个元素都取了出来
print(f"set转集合的结果是:  {set(my_set)}")
print(f"字典转 集合的结果是:{set(my_dict)}") # key值

# 通用排序sorted(容器,[reverse=True])给定容器进行排序
print(f"列表转 排序的结果是:{sorted(my_list,reverse=True)}")
print(f"元组转 排序的结果是:{sorted(my_tuple)}")
print(f"字符串转排序结果是: {sorted(my_str)}") # 每个元素都取了出来
print(f"set转排序的结果是:  {sorted(my_set)}")
print(f"字典转 排序的结果是:{sorted(my_dict)}") # key值

# 字符串比大小 同c语言一样,都是用ascii码值来比较的
# 按位比较,一位位对比,只要有一位大,那么整体就大,abd大于abc  ab大于a
print(f"abd大于abc:{"abd">"aab"}")
print(f"abasdf大于abc:{"abasdf">"aab"}")
print(f"abd大于a:{"abd">"a"}")
print(f"key2大于key1:{"key2">"key1"}")