# 掌握 ifelifelse 语句进行多条件判断的语法

# if 条件 1
# 条件 1 满足应做的事情
# 条件 1 满足应做的事情
# elif 条件 2:
# 条件 2 满足应做的事情
# 条件 2 满足应做的事情
# elif 条件 N:
# 条件 N 满足应做的事情
# 条件 N 满足应做的事情
# else:
# 所有条件都不满足应做的事情
# 所有条件都不满足应做的事情
print("欢迎来到牛马俱乐部")
# height = int(input("请输入你的身高(cm)"))
# vip_level = int(input("输入你的vip等级(1~5)"))

# if int(input("请输入你的身高(cm)")) < 120:
#     print("身高小于120cm,可以免费游玩")
# elif int(input("输入你的vip等级(1~5)")) > 3:
#     print("vip等级大于3,可以免费游玩")
# else:
#     print("joker,快补票!")
# print("祝你牛马当的开心")

# 2. 使用 ifelifelse 的注意点有:
# elif 可以写多个
# 判断是互斥且有序的，上一个满足后面的就不会判断了
# 可以在条件判断中，直接写 input 语句，节省代码量

# 练习
num = int(input("设定所猜数字:"))
if num == int(input("输入第一次猜的数字:")):
    print("猜对啦!")
elif num == int(input("不对,输入第二次猜的数字:")):
    print("猜对啦!")
elif num == int(input("不对,输入第三次猜的数字:")):
    print("猜对啦!")
else:
    print(f"全错,我设置的是{num}")