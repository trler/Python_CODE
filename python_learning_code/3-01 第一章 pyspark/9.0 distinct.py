# rdd数据进行去重，返回新rdd 无需传参

from pyspark import SparkConf, SparkContext
import  os

from pyspark.rdd import RDDBarrier
from pyspark.streaming.util import rddToFileName

os.environ['PYSPARK_PYTHON']= "C:/Users/ASUS/AppData/Local/Programs/Python/Python310/python.exe"
# conf = SparkConf.setMaster("local[*]").setAppName("test_spark")
conf = SparkConf().setMaster("local[*]").setAppName("Spark")
sc = SparkContext(conf=conf)
# 准备
rdd = sc.parallelize([1,2,3,4,5,1,6,3,2,4,7,4])

print(rdd.distinct().collect())
