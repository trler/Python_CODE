# 针对kv二元元组 自动按照key分组，根据聚合逻辑，完成组内数据value 的聚合操作
# (v,v) -> v 类型需要一样
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON']= "C:/Users/ASUS/AppData/Local/Programs/Python/Python310/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("Spark")
sc = SparkContext(conf=conf)

#
rdd = sc.parallelize([('男',99),('男',88),('女',99),('女',99)])
print(rdd.reduceByKey(lambda x,y:x+y).collect())
