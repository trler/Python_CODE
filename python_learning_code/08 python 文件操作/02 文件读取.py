# 1.了解文件操作的作用
# 2.掌握文件的打开、读取、关闭操作

# w 覆盖写入 不存在则创建文件
# a 追加内容不存在则创建
# r 读取文件, 光标在文件开头
f = open("data.txt", 'r', encoding='utf-8') # f里面有方法可以使用 类被实例化后的对象

# print(type(f))
# 读取文件 -read(num)方法 num表示读取字节,不写则全读取数据
# print(f"读取10个字节的效果:{f.read(4)}")
# print(f"read方法把所有字节读完的结果:{f.read()}") # 从光标开始读

# readlines() - 按行的方式把文件内容进行读取,并且返回一个列表,每一行的数据为一个元素
readlist = f.readlines()
print(f"readlist的类型是{type(readlist)}")
print(readlist)


