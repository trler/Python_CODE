# 城市销售额排行
# 全部城市,有哪些商品类别在售卖
# 北京市有哪些商品类别在售卖
# 构建执行环境入口对象
from pyspark import SparkConf, SparkContext
import  os
import json

from unicodedata import category

os.environ['PYSPARK_PYTHON']= "C:/Users/ASUS/AppData/Local/Programs/Python/Python310/python.exe"
# conf = SparkConf.setMaster("local[*]").setAppName("test_spark")
conf = SparkConf().setMaster("local[*]").setAppName("Spark")
sc = SparkContext(conf=conf)

# 读取文件 得到rdd
rdd1 = sc.textFile('order.txt')
# print(rdd1.collect())

# json字符串整理去掉 独立化
rdd2 = rdd1.flatMap(lambda line: line.split('|'))
# print(rdd2.collect())

# json字符串转成字典 map
dict_rdd = rdd2.map(lambda line: json.loads(line))
print(dict_rdd.collect())

# 取出城市和销售额的数据
# （城市，销售额）
result = (dict_rdd
          .map(lambda line: (line['areaName'],int(line['money'])))
          .reduceByKey(lambda x, y: x + y)
          .sortBy(lambda x:x[1],ascending=True,numPartitions=1)
          .collect()
)
print(result)

# 北京市有哪些商品类别在售卖
category_rdd = dict_rdd.map(lambda line: line['category']).distinct()
print(category_rdd.collect())

# 看北京有哪些类别在售卖
# 过滤
bj_catgory = dict_rdd.filter(lambda line: line['areaName'] == '北京').map(lambda line: line['category']).distinct()
print(bj_catgory.collect())

sc.stop()

# 此时此刻我