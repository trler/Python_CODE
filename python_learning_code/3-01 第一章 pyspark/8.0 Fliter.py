# 过滤想要的数据进行保留
# (T) ->BOOL

from pyspark import SparkConf, SparkContext
import  os

from pyspark.rdd import RDDBarrier
from pyspark.streaming.util import rddToFileName

os.environ['PYSPARK_PYTHON']= "C:/Users/ASUS/AppData/Local/Programs/Python/Python310/python.exe"
# conf = SparkConf.setMaster("local[*]").setAppName("test_spark")
conf = SparkConf().setMaster("local[*]").setAppName("Spark")
sc = SparkContext(conf=conf)
# 准备
rdd = sc.parallelize([1,2,3,4,5])
# 抛弃偶数 留下奇数
print(rdd.filter(lambda x: x % 2 != 0).collect())
