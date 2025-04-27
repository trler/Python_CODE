# 掌握 if else 语句的组合用法
# if else 语句，其中
# if 和其代码块，条件满足时执行
# else 搭配 if 的判断条件，当不满足的时候执行


# 2.ifelse 语句的注意事项:
# else 不需要判断条件，当 if 的条件不满足时，else 执行
# else 的代码块，同样要 4 个空格作为缩进

print("欢迎来到牛马动物园")
high = input("请输入你的身高:")
high = int(high)
if high > 120:
    print("您的身高于120cm.游玩需要补票10元")
else:
    print("您的身低于120cm,可以免费游玩")
print("祝您游玩愉快")