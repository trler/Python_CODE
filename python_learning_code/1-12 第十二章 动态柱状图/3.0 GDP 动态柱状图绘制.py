# 1.掌握列表的sort方法并配合lambda匿名函数完成列表排序
# 2.完成图表所需的数据处理
# 3.完成GDP动态图表绘制
from itertools import count
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import *


time = Timeline({"theme":ThemeType.DARK})
# 列表.sort(key=排序函数,reverse=True|False)
my_list = [["a",1],["b",3],["c",2]]

def choose_sort_key(element):
    return element[1]

my_list.sort(key=choose_sort_key,reverse=True)
my_list.sort(key=lambda element: element[1],reverse=True)
print(my_list)

# 数据处理
f = open("./动态柱状图数据/1960-2019全球GDP数据.csv","r",encoding="GB2312")
data_lines=f.readlines()
f.close()
# print(data_lines)
# 删除第一行
data_lines.pop(0)
# print(data_lines)

# 构建字典 {"年份":[国家gdp列表],"年份2":[国家gdp列表]}
dict1 = {}
for line in data_lines:
    line=line.strip()
    yaer = int(line.split(",")[0])
    country = line.split(",")[1]
    country_GDP = float(line.split(",")[2])
    # 判断有没有对应的年份 即key,没有创建一个空列表加进去 然后继续append
    try:
        dict1[yaer].append([country,country_GDP])
    except KeyError:
        dict1[yaer] = []
        dict1[yaer].append([country,country_GDP])
# print(dict1)

# 排序年份
sorted_year= sorted(dict1.keys())
# print(sorted_year)
for year in sorted_year:

# 排序每一年里面的gpd大小,取前八
    dict1[year].sort(key=lambda element: element[1],reverse=True)
    # 取出前八国家
    year_data = dict1[year][:8]
    year_data.reverse()
    x_data = []
    y_data = []
    for element in year_data:
        x_data.append(element[0])
        y_data.append(element[1]/10000000)

    # 构造数据图
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data,label_opts=LabelOpts(position="right"))
    # 反转xy
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP"),
    )
    #创建时间线对象年份 名字
    time.add(bar,str(year))
time.add_schema(
    play_interval=500,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
)
time.render("动态GDP.html")









