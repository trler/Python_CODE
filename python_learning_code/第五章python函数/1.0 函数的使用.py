# str = input("输入所求长度的字符串")
# i = 0
# for x in str:
#     i += 1
# print(f"输入的字符串长度为{i}个长度")
while(True):
    def my_len(date):
        count = 0
        for i in date:
            count +=1
        print(f"字符串长度为{count}")
    str = input("输入所求长度的字符串")
    my_len(str)