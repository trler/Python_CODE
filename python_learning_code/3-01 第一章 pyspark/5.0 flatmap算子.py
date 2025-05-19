# 相比于map flatmap可以解除嵌套操作

# 嵌套list [[],[[],[]]] 可以变成[]

from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON']= "C:/Users/ASUS/AppData/Local/Programs/Python/Python310/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("Spark")
sc = SparkContext(conf=conf)

# 准备一个rdd
rdd = sc.parallelize(['itheima itcast 666','itherima itheirm itcast','python itheima'])

#
print(rdd.map(lambda x:x.split(' ')).collect()) # 此时是嵌套格式的
print(rdd.flatMap(lambda x:x.split(' ')).collect())