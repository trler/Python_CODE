# 为什么使用类型注解
# pycharm中的list.后会有自动提示可用方法   为什么可以做到这一点 pycharm怎如何知道有append方法
# 因为,pycharm可以确定是list类型
#
# 但是  def func(data):
#          data.append(1)# pycharm 确定是list是什么类型
import json
import random

# python 可以显示的利用类型注解,将data注解为list pycharm可以识别到
# 可以对 变量 和函数返回值与形参进行注解

# 语法 变量:类型
var_1 : int = 10
var_2 : float = 3.1313
var_3 : bool = True
var_4 : str = "蛤目的和爸爸"

# 类对象注解
class phone:
    def call_by_4g(self):
        print(f"{self.__class__.__name__}.call_by_4g()")
stu: phone = phone()

# 数据容器注解 还可以详细注解 给里面的元素类型也标记出来
my_list1:list =[1,2,3]
my_tuple1 : tuple = ("intheima",666,True)
my_dict1 : dict = {"name": 1123}
my_set1: set = {1,2,3}

my_list:list[int] =[1,2,3]
my_tuple : tuple[str,int,bool] = ("intheima",666,True)
my_dict : dict[str,int] = {"name": 1123}
my_set: set[int] = {1,2,3}

# 掌握变量的类型注解方式 也可以在注释中进行注解

class student:
    pass
def func():
    return  1

var_11 =random.randint(1, 10) # type:int
var_21 = json.loads('{"name":"liche"}') # type: dict[str,str]
var_31  = func() # type:int

# 一般来说 上面的基本上不会去写
# josn.loads 会自动识别

化身美


