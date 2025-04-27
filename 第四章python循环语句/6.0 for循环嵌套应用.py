#小美表白
# i = 1
# for x in range(100):
#     print("今天是表白的第%d天" % (x+1))
#     for y in range(10):
#         print(f"第{x+1}天送出第{y+1}朵花")
#     print(f"小美,我喜欢你")
# print(f"第{x+1}天,表白成功")

# 99乘法表
n = int(input("输入想要的乘法表阶数"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(f"{i}*{j}={(i*j)}\t", end = ' ')
    print()
