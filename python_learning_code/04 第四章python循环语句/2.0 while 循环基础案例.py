import random
num = random.randint(1, 100)
tmp = 1
# guess_num = int(input(f"第{tmp}次猜,请输入你的数字"))
# while(guess_num!= num):
#     tmp += 1
#     if guess_num > num:
#         print("猜大了")
#     else :
#         print("猜小了")
#     guess_num = int(input(f"第{tmp}次猜,请输入你的数字"))
# print(f"猜了{tmp}次,这个数字是{num}")
flag = True
while(flag):
    guess_num = int(input(f"第{tmp}次猜,请输入你的数字"))
    if guess_num == num:
        print("猜对了")
        flag  = False
    elif guess_num > num:
        print("猜大了")
        tmp += 1
    else :
        print("猜小了")
        tmp += 1
print(f"猜了{tmp}次,这个数字是{num}")