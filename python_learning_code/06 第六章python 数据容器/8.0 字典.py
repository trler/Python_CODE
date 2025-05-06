# 字典的定义
# 通过key 找到 value
# key 关键信息,来找到value的数值
# 老师有一份信息,student的名称和成绩 ,可以用学生姓名找到成绩 使用字典比较合适
# 字典也用{} 但是存储的元素是一个一个的键值对

# 定义字典字面量{key: value, key: value, ......key: value}
#定义字典变量my_dict = {key: value, key: value, ....., key:value}
#定义空字典
#空字典定义方式1my_dict = {}
#空字典定义方式2my_dict = dict()

my_dict = {"王力宏": 99, "神人": 10000, "周绝伦": 111, "林俊杰": 99999}
my_dict2 = {}
my_set = set()
my_dict3 = dict()
print(f"字典1的内容为{my_dict},类型为{type(my_dict)}")
print(f"字典1的内容为{my_dict2},类型为{type(my_dict2)}")
print(f"字典1的内容为{my_dict3},类型为{type(my_dict3)}")
# 自然不能重复 不能使用下表索引 同set一样
# 但是可以通过key来取到对应的value

print(my_dict["王力宏"])
# key不为字典情况下,可以是任意数字类型 value也可以是字典 可以嵌套

# 字典嵌套
# stu_yuwen_score = {"王力宏": 77 , "周杰伦": 88 ,"凌俊杰" : 99}
# stu_math_score = {"王力宏": 66 , "周杰伦": 86 ,"凌俊杰" : 96}
# stu_english_score = {"王力宏": 33 , "周杰伦": 55 ,"凌俊杰" : 66}
stu_score = {
    "语文":{
        "王力宏": 77 ,
        "周杰伦": 88,
        "凌俊杰": 99
    },"数学":{
        "王力宏": 66 ,
        "周杰伦": 86 ,
        "凌俊杰": 96
    },"英语":{
        "王力宏": 33 ,
        "周杰伦": 55 ,
        "凌俊杰":66}
}
print(stu_score)

stu1_score = {"语文": 77 ,"数学": 66,"英语":33}
stu2_score = {"<UNK>": 88 ,"<UNK>": 86,"<UNK>":55}
stu3_score = {"语文": 99 ,"数学": 96,"英语":66}
stu1 = {"姓名": "王力宏" ,"各科分数": stu1_score}
stu2 = {"姓名": "周杰伦" ,"各科分数": stu2_score}
stu3 = {"姓名": "林俊杰" ,"各科分数": stu3_score}# 不太可以从key中找到 value
print(f"{stu1},{stu2},{stu3}")
stu_score_dict = {
    "王力宏": {
        "语文": 77,
        "数学": 66,
        "英语": 33
    },"周杰伦":{
        "语文": 88,
        "数学": 86,
        "英语": 55
    },"凌俊杰":{
        "语文": 99,
        "数学": 96,
        "英语": 66
    }
}
print(stu_score_dict)

# 从嵌套dict中获取信息
score  = stu_score_dict["周杰伦"]["语文"]
score2  = stu_score_dict["凌俊杰"]["英语"]
print(f"周杰伦的语文成绩为{score}")
print(f"周杰伦的语文成绩为{score2}")


# 相关操作

# 新增元素 dict[key] = value 如果key不存在 新增元素
dict1 = {"张学友": 11, "张兴哲":66 ,"周绝伦":33}
dict1["山乐山大佛"] = 33
print(f"字典新增元素{dict1}")

# 更新元素 dict[key] = value 如果key存在 更新元素
dict1["张学友"] = "即将变成了上饿啊是否"
print(f"字典修改元素{dict1}")

# 删除元素 dict.pop(key)
element1 = dict1.pop("张学友")
print(f"删除张学友后变成{dict1},被删除的人的分数变为  {element1}")

# 清空元素 dict.clear
dict1.clear()
print(f"字典被清空了{dict1}")

# 获取全部key dict.keys() 得到字典中的所有key
dict1 = {"零明珠": 11, "王绍芬":66 ,"周杰伦":33}
print(f"拿出来所有的key为{dict1.keys()}")

# 方式一 遍历字典 利用keys 获得所有的key
for element in dict1.keys():
    print(f"dict1中的key为{element}")
    print(f"{element}的value是{dict1[element]}")

# 方式二 直接for循环
for element in dict1:
    print(f"dict1中的key为{element}")
    print(f"{element}的value是{dict1[element]}")

# 统计字典元素数量 len()
num  = len(dict1)
print(f"{num}个")

# 作业 员工信息操作
worker_dict = {
    "王力宏":{
        "部门": "科技部",
        "工资": 3000,
        "级别": 1,
    },
    "周杰伦":{
        "部门": "市场部",
        "工资": 5000,
        "级别": 2,
    },
    "凌俊杰":{
        "部门": "市场部",
        "工资": 7000,
        "级别": 3,
    },
    "张学友":{
        "部门": "科技部",
        "工资": 4000,
        "级别": 1,
    },
    "刘德华":{
        "部门": "市场部",
        "工资": 6000,
        "级别": 2,
    }
}
for worker_name in worker_dict.keys():
    if worker_dict[worker_name]["级别"] == 1:
        worker_dict[worker_name]["工资"] += 1000
        worker_dict[worker_name]["级别"] += 1
print(worker_dict)