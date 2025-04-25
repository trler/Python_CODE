# 数据类型之间,在特定的场景下,是可以相互转换的,字符串转成数字,数字转换字符串
# 数据类型转换的应用场景
# 从文件中读取的数字，默认是字符串，需转换成数字类型。
# input()语句默认结果是字符串，若需数字，也需转换。
# 将数字转换成字符串，用于输出到外部系统 。

# int(x)	将x转换为一个整数
# float(x)	将x转换为一个浮点数
# str(x)	将对象x转换为字符串 三个都具有返回值

# 语法结构表示：Python 没有像 C 语言那样用大括号 {} 来明确界定代码块，而是采用缩进来表示代码块的层次结构。
# 例如在 if、for、while 等语句以及函数定义中，缩进的代码属于对应的代码块。如果缩进混乱，Python 解释器就无法准确判断代码块的边界，导致程序逻辑错误 。比如：

num_str = str(11)
print(type(num_str),num_str)
float_str = str(3.14)
print(type(float_str),float_str)
string_int = int("3")
print(type(string_int),string_int)
float_int = int(3.14)
print(type(float_int),float_int)
int_float = float(3)
print(type(int_float),int_float)

