# continue关键字用于:中断本次循环,直接进入下一次循环
# continue可以用于:
# for循环和while循环,效果一致

# for x in range(1,6):
#     print(x)
#     continue
#     print("执行了2")

# 左侧代码:
# 在循环内,遇到break就结束循环了
# 所以,执行了语句1后,直接执行语句3了
# break关键字同样只可以控制:它所在的循环结束
for i in range(1,101):
    print("语句1")
    for j in range(1,10):
        print("语句2")
        break
        print("语句3")
    print("语句4")
    break
