# 输出到文件中
# saveAsTextFile 算子 路径 方法
from pyspark import SparkConf, SparkContext
import  os
os.environ['PYSPARK_PYTHON']= "C:/Users/ASUS/AppData/Local/Programs/Python/Python310/python.exe"
os.environ['HADOOP_HOME'] ="C:/Users/ASUS/Downloads/hadoop-3.3.6"  # 配置hadoop相关依赖 即可
conf = SparkConf().setMaster("local[*]").setAppName("Spark")
# conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)
# rdd1
rdd1 = sc.parallelize([1,2,3,4,5],numSlices=1)
# rdd2
rdd2 = sc.parallelize([("hello",3),("spark",4),("hi",5)],numSlices=1)
# rdd3
rdd3 = sc.parallelize([[1,3,5],[6,7,9],[11,13,11]],numSlices=1)


# 输出到文件中 文件名而不是文件夹
rdd1.saveAsTextFile('D:/111/output1')
rdd2.saveAsTextFile('D:/111/output2') # 依赖hadoop依赖 下载 解压 下载winutils.exe放入bin  下载hadoop.dll放入
rdd3.saveAsTextFile('D:/111/output3')


# 更改rdd1为一个分区
# pyspark3.5.5 用hadoop3.3.6


# sparkconf对象设置属性全局设置为1
# 创建rdd时候设置为 numSlices为1