
# JSON是一种轻量级的数据交互格式。可以按照JSON指定的格式去维织和封装数据
# JSON本质上是一个带有特定格式的字符串
# 主要功能:json就是一种在各个编程语言中流通的数据格式,负责不同编程语言中的数据传递和交互.类似于:
# 国际通用语言-英语    中国56个民族不同地区的通用语言-普通话
# json 的数据格式要求很严格 但是和pyhton格式是无缝切换的, 列表,字典形式一样 列表里面嵌套字典就是json
#

# python json 的互相转换
import json

# 准备符合json格式的python数据 一个列表, 列表里面元素是字典
data  = [{"name":"长大三","age": 11},{"name":"阿斯蒂芬","age": 13},{"name":"长阿萨","age": 133}]
json_str = json.dumps(data,ensure_ascii=False) # 后面参数转换编码 不使用ascii码转换 否则变成unicode
print(type(json_str)) # 字符串
print(json_str) # 变成unicode了

# 将python转换为json
d = {"name":"周杰伦","age":"台北"}
json_str = json.dumps(d,ensure_ascii=False) # 后面参数转换编码 不使用ascii码转换 否则变成unicode
print(type(json_str)) # 字符串
print(json_str) # 变成unicode了

# 将json转换为python
s = '[{"name": "长大三", "age": 11}, {"name": "阿斯蒂芬", "age": 13}, {"name": "长阿萨", "age": 133}]'
l = json.loads(s)
print(type(l)) # 列表类型
print(l) # 列表 可以进行操作

# 字典格式的json
s = '{"name": "周杰伦", "age": "台北"}'
d = json.loads(s)
print(type(d))
print(d)
