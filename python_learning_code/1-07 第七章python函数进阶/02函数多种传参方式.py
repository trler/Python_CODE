# 1.掌握位置参数
# 位置参数:调用函数时根据函数定义的参数位置来传递参数

# 2.掌握关键字参数
# 关键字参数:函数调用时通过键=值形式传递参数.
# 作用:可以让函数更加清晰、容易使用,同时也清除了参数的顺序需求
def user_info(name,age,gender):
    print(f"你的名字是:{name},年龄是:{age},性别是:{gender}")
user_info(name="西格玛",age=20,gender="楠") # 形参 = 实参 键值对
user_info(age=20,name="西格玛",gender="楠") # 打乱顺序
user_info("小西格玛",gender="楠",age=20) # 混用位置参数 位置参数必须在前面

# 4.掌握缺省参数

# 缺省参数:缺省参数也叫默认参数,用于定义函数,为参数提供默认值,调用函数时可不传该默认参数的值
# 注意: 所有位置参数必须出现在默认参数前,包括函数定义和调用)
# 作用:当调用函数时没有传递参数,就会使用默认是用缺省参数对应的值.
def user_info(name,age,gender='楠'):
    print(f"你的名字是:{name},年龄是:{age},性别是:{gender}")
user_info("神人",13,gender="变性人")

# 3.掌握不定长参数 可变参数 不确定调用时候会传入多少参数
# 位置传递不定长
def user_info(*args): # 元组
    print(f"传入参数为:{args}")
user_info("<UNK>","<UNK>","<UNK>")
# 传进的所有参数都会被args变量收集, 它会根据传进参数的位置合并为一个元组(tuple), args是元组类型, 这就是位置传递

# 关键字传递不定长
def user_info(**kwargs): #字典
    print(f"字典为:{kwargs}")
user_info(name="哈姆",age=12,gender="变性人")
# 参数是"键=值"形式的形式的情况下,所有的"键=值"都会被kwargs接受,同时会根据"键=值"组成字典




