from pyspark import SparkConf, SparkContext
import  os
os.environ['PYSPARK_PYTHON']= "C:/Users/ASUS/AppData/Local/Programs/Python/Python310/python.exe"
os.environ['HADOOP_HOME'] ="C:/Users/ASUS/Downloads/hadoop-3.3.6"  # 配置hadoop相关依赖 即可
conf = SparkConf().setMaster("local[*]").setAppName("Spark")
conf.set('spark.default.parallelism', "1")
# conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)


# 搜索引擎日志 读取文件 转换成rdd  # 本质上三个均为数数单词模型
file_rdd  = sc.textFile("search_log.txt")

# 打印输出 热门搜索时间段 小时精度 top3
result0 = file_rdd.map(lambda line: line.split("\t")) # map对每个元素分别进行处理
# print(result0.collect())
result1 = file_rdd.map(lambda x: (x.split('\t')[0][:2],1)).\
    reduceByKey(lambda x,y:x+y).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3)
print(result1) # 打印结果
# print(file_rdd.collect())


# 打印输出 热门搜索词
result2 = file_rdd.map(lambda x: (x.split('\t')[2],1)).\
    reduceByKey(lambda x,y:x+y).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3) # 选数据 并元祖 累加 排序 取前三
print(result2)

# 打印输出 统计黑马程序员关键字在哪个搜索时段最多
result3 = file_rdd.map(lambda x: x.split('\t')).\
    filter(lambda x: x[2] == '黑马程序员').\
    map(lambda x:(x[0][:2],1)).\
    reduceByKey(lambda x,y:x+y). \
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3)
print(result3)

# 将数据转换为json 写出为文件
file_rdd.map(lambda x:x.split('\t')).\
    map(lambda x: {"time":x[0] , "user_id":x[1], "key_word":x[2], "rank1":x[3] , "rank2":x[4] , "url":x[5]}).\
    saveAsTextFile('D:/OUTPUT1')