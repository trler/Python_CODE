import json
from pyecharts.charts import Line
from pyecharts import options
from pyecharts.options import TitleOpts, LegendOpts, LabelOpts

# 处理数据
f_us = open("./折线图数据/美国.txt","r",encoding="utf-8")
us_data = f_us.read()
f_jp = open("./折线图数据/日本.txt","r",encoding="utf-8")
jp_data = f_jp.read()
f_in = open("./折线图数据/印度.txt","r",encoding="utf-8")
in_data = f_in.read()

# 去除不规范 不符合json规则的开头
us_data = us_data.replace("jsonp_1629344292311_69436(","")
jp_data = jp_data.replace("jsonp_1629350871167_29498(","")
in_data = in_data.replace("jsonp_1629350745930_63180(","")
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]



# json 转python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# print(type(us_dict))
# print(us_dict) # 变成字典了

# 获取trend key
us_trend_data=us_dict["data"][0]["trend"]
jp_trend_data=jp_dict["data"][0]["trend"]
in_trend_data=in_dict["data"][0]["trend"]
# print(us_trend_data)

# 获取日期数据
us_x_data = us_trend_data["updateDate"][:314]
jp_x_data = jp_trend_data["updateDate"][:314]
in_x_data = in_trend_data["updateDate"][:314]

print(us_x_data)
print(jp_x_data)
print(in_x_data)

# y轴数据 list 里面的数据是列表0号确诊信息
us_y_data = us_trend_data["list"][0]["data"][:314]
jp_y_data = jp_trend_data["list"][0]["data"][:314]
in_y_data = in_trend_data["list"][0]["data"][:314]
print(us_y_data)
print(jp_y_data)
print(in_y_data)

line=Line()
# 添加x轴数据
line.add_xaxis(us_x_data);

# 添加y轴数据
line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数",in_y_data,label_opts=LabelOpts(is_show=False))  # 系列属性


# 设置全局选项
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts()
)



#
line.render()



f_in.close()
f_us.close()
f_jp.close()
