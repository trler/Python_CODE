# 掌握逻辑判断语句 (if) 的基本语法格式
# 掌握布尔类型数据，在判断语句中的作用
from inspect import AGEN_CLOSED

# age = input("输入你的年龄")
# age = int(age)
# if age>= 2: #一个布尔类型:
#     print("你还是joker")
#     print("而且你是老登")
# else:
#     print("你是joker")
#     print("你马上变成老登")
print("欢迎来到动物园,儿童免费,成人收费")
age = input("输入你的年龄")
age = int(age)
if age>= 18: #一个布尔类型:
    print("您已经大于18岁",end = " ")
    print("补票10元!")
else:
    print("你是joker")
    print("不用补票")

