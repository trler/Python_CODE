# 依赖rdd内置丰富的 成员方法（算子）

# map算子 将rdd的数据一条条处理，基于map算子接受的函数 然后返回新的rdd


from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON']= "C:/Users/ASUS/AppData/Local/Programs/Python/Python310/python.exe"

# os.environ['PYSPARK_PYTHON']= "E:\dev\python\python3.13\python.exe"
# os.environ['PYSPARK_DRIVER_PYTHON'] = "E:/dev/python/python3.10/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("Spark")
sc = SparkContext(conf=conf)

# 准备rdd
rdd = sc.parallelize([1, 2, 3, 4, 5])

# 通过map方法 将每个元素*5
# def func(data):
#     return data*100

rdd2 = rdd.map(lambda x: x*10).map(lambda x: x*10) # 报错还需要其他代码 spark找不到python

# (T) -> U
# (T) -> T
print(rdd2.collect())