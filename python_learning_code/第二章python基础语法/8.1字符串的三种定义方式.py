# 字符串可以用''  ""  """""" 来定义
# 其中 """""" 给变量赋值时 不是注释
name = """黑马 程序元"""
print(name)
name_1 = "黑马"
print(name_1)
name_2 = '黑马'
print(name_2)

# 如果定义字符串 包含引号 怎么办 单引号定义可以用双引号 二者交叉使用
#  转移字符\
print("我人杀了\"")
name_3 = '"我来了"'
print(name_3)
name_4 = "'wo1'"
print(name_4)
print("\"我人杀了\"")