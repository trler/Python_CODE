"""
面向对象,数据分析案例,主业务逻辑代码
实现步骤:

1.设计一个类,可以完成数据的封装
2.设计一个抽象类,定义文件读取的相关功能,并使用了子类实现具体功能
3.读取文件,生产数据对象
4.进行数据需求的逻辑计算(计算每一天的销售额)
5.通过PyEcharts进行图形绘制

"""
from gzip import WRITE
from json.decoder import WHITESPACE

from pandas.core.internals.construction import dataclasses_to_dicts

from file_define import *
from data_define import *
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import *

from pymysql import Connection

text = textfile_reader("2011年1月销售数据.txt")
json1 = json_reader("2011年2月销售数据JSON.txt")

jan_data :list[Record] = text.read_data()
feb_data :list[Record] = json1.read_data()

# 将两个月合并为一个all_list
all_data :list[Record] = jan_data + feb_data

# print(all_data)
# 构建mysql数据库链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="lcx1234321",
    autocommit=True,
)

# 获得游标对象
cursor = conn.cursor()


# 选择数据库
conn.select_db("py_sql")

# 组织数据库语句
for record in all_data:
    sql = (f"insert into orders(order_date,order_id,money,province) "
           f"values('{record.date}','{record.order_id}',{record.money},'{record.province}')")
    cursor.execute(sql)
    # print(sql)
# 执行sql语句



# 关闭对象
conn.close()

# 数据计算
# # 利用for 和字典匹配  将每一天的相加
# data_dict =  {}
# for data in all_data:
#     try: data_dict[data.date] += data.money
#
#     except: data_dict[data.date] = data.money
#     ### 或者用 if else也行
# print(data_dict)
#
# # 可视化对象开发
# bar = Bar(init_opts=InitOpts())
# bar.add_xaxis(list(data_dict.keys()))
# bar.add_yaxis("销售额", list(data_dict.values()),label_opts=LabelOpts(is_show=False))
# bar.set_global_opts(
#     title_opts=TitleOpts(title="每日销售额"),
#
# )
# bar.render("每日销售额.html")




