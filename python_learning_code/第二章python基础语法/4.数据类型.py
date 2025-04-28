# type()语句来查看数据类型
# 理解变量无类型而数据有类型的概念
# 数据类型 string int float
print(type("world"))
print(type(8888))
print(type(13.4))# 查看字面量的数据类型
int_type = type(888)
float_type = type(1.2)
string_type = type("he")
print(int_type)# 查看 储存了类型的变量
print(float_type)# 查看
print(string_type)# 查看

# 方式3
name = "黑马"#查看变量的数据类型
name_type = type(name)
print(name_type)
# python 是一种动态类型语言 实在变量的数据是在赋值时自动确定的
