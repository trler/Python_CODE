# 定义一个数字随机产生), 通过 3 次判断来猜出来数字
import random
num = random.randint(1,10)
guess_num1 = int(input("猜测1-10中的数字:"))
if guess_num1 == num:
    print("第一次就猜对了")
else :
    if guess_num1 > num:
        print("猜大了,重新猜")
    else:
        print("猜小了,重新猜")
    guess_num2 = int(input("第二次猜测的数字为:"))
    if guess_num2 == num:
        print("第二次猜对了")
    else :
        if guess_num2 > num:
            print("猜大了,重新猜")
        else:
            print("猜小了,重新猜")
        guess_num3 = int(input("第二次猜测的数字为:"))
        if guess_num3 == num:
            print("第二次猜对了")
        else:
            if guess_num2 > num:
                print(f"猜大了,次数用尽随机数是{num}")
            else:
                print(f"猜小了,次数用尽随机数是{num}")