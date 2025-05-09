# 理解使用对象来完成数据组织的思路
# 生活中 设计表格 打印表格 填写表格
# 程序中 设计类   创建对象 对象属性赋值 类似于结构体

# 设计一个类
class Student:
    name = None
    gender = None
    age = None
    nationality = None
    native_place = None

# 创建一个对象
stu_1 = Student()
stu_2 = Student()

# 赋值对象属性
stu_1.age = 20
stu_1.gender = '楠'
stu_1.nationality = '中国'
stu_1.native_place = '啥动人'
stu_1.name = '凌俊杰'

# 获取对象中记录的信息
print(stu_1.age)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.name)
print(stu_1.gender)















