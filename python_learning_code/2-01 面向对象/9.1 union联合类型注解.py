# union 类型
my_list: list[int] = [1, 2, 3]
my_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3} # 可以很好注解

# 但如果 混合数据类型呢? 用混合类型 # 需要导包 
from typing import Union
my_list1 : list[Union[int,str]] = [1, 2, 3,"stsd"]
my_dict1 : dict[str,Union[str,int]] = {"a": 1, "b": 2, "c": 3}

# 形参 返回值,也可以使用
def func(data:Union[int,str]) -> Union[int,str]:
    pass