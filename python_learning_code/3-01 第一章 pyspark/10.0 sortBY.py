#　自定义一局拍雪
# rdd.sortby(func,ascending=False , numPartitions = 1)
# func告诉按照rdd的那个数据进行排序，比如lambda x：x[1] 按照第二个进行排序的
# ascending t升，f下
# numpartitions:用多少分区排序

# 读取文件hellotxt 利用spark统计单词出现数量
from ctypes.wintypes import PWORD

# 构建执行环境入口对象
from pyspark import SparkConf, SparkContext
import  os

from pyspark.streaming.util import rddToFileName

os.environ['PYSPARK_PYTHON']= "C:/Users/ASUS/AppData/Local/Programs/Python/Python310/python.exe"
# conf = SparkConf.setMaster("local[*]").setAppName("test_spark")
conf = SparkConf().setMaster("local[*]").setAppName("Spark")
sc = SparkContext(conf=conf)

# 读取文件
rdd1 = sc.textFile('hello.txt')

# 切分单词
word_rdd = rdd1.flatMap(lambda line: line.split(' '))
# print(rdd2.collect())

# 将所有的单词都转换为 二元元组，单词为key， value设置为1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
# print(word_with_one_rdd.collect())

# 分组求和
result_rdd=word_with_one_rdd.reduceByKey(lambda x, y: x + y)
#
print(result_rdd.collect())
#

#　对结果集　进行排序　按照次数从大到小进行排序ａ
print(result_rdd.sortBy(lambda x: x[1],ascending=False,numPartitions=1).collect())


sc.stop()