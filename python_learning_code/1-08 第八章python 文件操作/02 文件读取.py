# 1.了解文件操作的作用
# 2.掌握文件的打开、读取、关闭操作

# w 覆盖写入 不存在则创建文件
# a 追加内容不存在则创建
# r 读取文件, 光标在文件开头
# f = open("data.txt", 'r', encoding='utf-8') # f里面有方法可以使用 类被实例化后的对象

# print(type(f))
# 读取文件 -read(num)方法 num表示读取字节,不写则全读取数据
# print(f"读取10个字节的效果:{f.read(4)}")
# print(f"read方法把所有字节读完的结果:{f.read()}") # 从光标开始读

# readlines() - 按行的方式把文件内容进行读取,并且返回一个列表,每一行的数据为一个元素
# readlist = f.readlines()
# print(f"readlist的类型是{type(readlist)}")
# print(readlist)

# readline 一次读取一行内容
# line1 = f.readline()
# print(f"line1的数据为{line1}")

# for循环读取文件
# i = 1
# for line in f:
#     print(f"第{i}行的数据是:{line}")
#     i += 1
# import time

# 文件关闭 close()
# f.close()
# time.sleep(1)

# # withopen 语法文件
# with open("data.txt", 'r', encoding='utf-8') as f:
#     for line in f:
#         print(f"利用withopen 打开文件 输出第n行为{line}")



# 作业 统计itheima 单词出现的次数
# with open("word.txt", 'r', encoding='utf-8') as f:
    # 方法1 readlines 读取成列表,然后分别统计 列表每一位置上的itheima数据 统计后相加
    # num_list = f.readlines()
    # print(num_list)
    # num = 0;
    # for i in num_list:
    #     num += i.count("itheima")
    # print(num)

    # 方法2 read() count 返回所有字符串 搜索itheima字符串顺序
    # content = f.read()
    # num = content.count("itheima")
    # print(num)

    # 方法3 for循环 将每一行读取,返回字符串,将字符串处理\n 后, split 分割成单词 统计出单词数量
    # count = 0
    # for line in f:
    #     line = line.strip()
    #     words = line.split(" ")
    #     for word in words:
    #         if word == "itheima":
    #             count += 1
    #
    # print(count)

