# 我们会发现，这个拼接字符串也不好用啊
# 1. 变量过多，拼接起来实在是太麻烦了
# 2. 字符串无法和数字或其它类型完成拼接。
# 字符串格式化 支持 拼接＋各种类型 占位型拼接
name = "黑马程序员"
message = "我叫%s,我电话是%s" % (name,3342)#和c不同 可以直接转换类型

print(message)

# 多个变量占位
# 变量要用括号括起来
# 并按照占位的顺序填入
class_num = 57
avg_salary = 16781
message = "python大数据科学,第%s班,代码%d人" % (class_num,avg_salary)
print(message)

# %表示我要占位
# s表示变成字符串
# d表示变成整数
# f表示变成浮点型
name = "传播媒体"
set_up_year = 2006
stock_price = 19.99
message = "我是%s,今年是%d年,股价是%f " % (name,set_up_year,stock_price)
print(message)# 精度出现问题 没有进行控制

