# RDD 对象
# 弹性分布式数据集（resilient distributed datasets）
# pyspark针对数据的处理，都是以RDD为对象作为载体的，



from pyspark import SparkConf, SparkContext

conf = SparkConf()

conf.setAppName("spark").setAppName("test_spark")
sc = SparkContext(conf=conf)

# parallelize 方法
rdd1 = sc.parallelize([1,2,3,4,5])
rdd2 = sc.parallelize((1,2,3,4,5))
rdd3 = sc.parallelize("abcdef")
rdd4 = sc.parallelize({1,2,3,4,5})
rdd5 = sc.parallelize({"key1":"value1","key2":"value2"})

# 查看rdd1 需要collect() 方法
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())




