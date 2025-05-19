# python对象,文件变成rdd rdd自己计算,在返回位python对象或者文件
# collect算子
# collect 将rdd各个分区中全部数据 统一收集到driver中 转变为一个list对象

from pyspark import SparkConf, SparkContext
import  os
os.environ['PYSPARK_PYTHON']= "C:/Users/ASUS/AppData/Local/Programs/Python/Python310/python.exe"
from unicodedata import category
conf = SparkConf().setMaster("local[*]").setAppName("Spark")
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize([1,2,3,4,5])
print(rdd1) # 无法输出 只能输出类型
rdd1_list: list = rdd1.collect()
print(rdd1_list)
print(type(rdd1_list))

# reduce算子 两两聚合  而reducebykey按照key分组
rdd2 = sc.parallelize([(1,2),(3,4),(5,6),(7,8)])
rdd2_tuple = rdd2.reduce(lambda x,y:x+y)
print(rdd2_tuple)

rdd21= sc.parallelize([1,2,3,4,5,6,7])
num  = rdd1.reduce(lambda x,y:x+y)
print(num)

# take 算子 取出前三个 组成list
take_list = rdd1.take(3)
take_list2 = rdd2.take(3)
print(take_list2)
print(take_list)

# count 统计rdd中有多少条数据 返回数字
num1 = rdd1.count()
num2 = rdd2.count()
print(num1)
print(num2)