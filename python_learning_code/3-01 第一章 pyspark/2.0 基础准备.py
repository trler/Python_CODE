# 安装pyspark

# pyspark执行环境入口对象 SparkContext

# 导包
from pyspark import SparkConf, SparkContext

# 创建sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("Spark")

# 基于sparkconf类对象，构建sparkcontext 类对象
sc = SparkContext(conf=conf)

# 打印pyspark相关运行版本
print(sc.version)

# 停止
sc.stop()


# 编程 模型 sparkcontext 类对象 是入口
# 数据输入 数据处理 数据输出
# 通过sparkcontext成员方法，完成数据读取吗得到RDD类对象
# RDD类对象成员方法，进行计算
# 调用各种成员方法 将rdd对象输出


