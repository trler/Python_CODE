import json
from pyecharts.charts import Map
from pyecharts.options import *

# 导入数据
f = open("./地图数据/疫情.txt","r",encoding="utf-8")
data = f.read()
f.close()

# json 转换为 python的字典
province_data_dict = json.loads(data)["areaTree"][0]["children"][3]["children"]
# print(province_data_dict)

# for循环 组装每个省份和人数组成元组,封装到列表中
data_list =[]
for province_data in province_data_dict:
    province_name = province_data["name"]+"市"
    # print(province_name)
    province_confirmed = province_data["total"]["confirm"]
    print(province_confirmed)
    data_list.append((province_name,province_confirmed))
print(data_list)

# map对象
map = Map()

# 添加数据
map.add("河南确诊人数",data_list,maptype="河南")

# 设置全局变量
map.set_global_opts(
    title_opts=TitleOpts(title="河南确诊人数"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1-99人","color":"#CCFFFF"},
            {"min":100,"max":999,"label":"100-999人","color":"#f9ed69"},
            {"min":1000,"max":4999,"label":"1000-4999人","color":"#f08a5d"},
            {"min":5000,"max":9999,"label":"5000-9999人","color":"#b83b5e"},
            {"min":10000,"max":99999,"label":"10000-99999人","color":"#6a2c70"},
            {"min":100000,"label":"大于100000","color":"#522546"}
        ]
    )

)

# render
map.render("河南疫情.html")