# print("hello world", end = ' ')
# print("hello world")#不换行的 hello , 空的python文件
#制表符\t


# 打印99乘法表 自定义大小乘法表
n = int(input("输入乘法表的行列数n = "))
j = 1
while j<=n:
    i = 1
    while i < j:
        print(f"{i}*{j}={(i*j)}\t", end = ' ')
        i +=1
    print(f"{i}*{j}={(i*j)}")# print() 就是换行
    j = j+1

# j来控制第j行,i来控制每一行的列遍历



