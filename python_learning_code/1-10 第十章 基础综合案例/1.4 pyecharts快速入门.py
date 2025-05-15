# 基础折线图 导入Line功能构建折线图对象
from pyecharts.charts import Line as li # 导包
from pyecharts.options import TitleOpts, LegendOpts, TooltipOpts, VisualMapOpts, ToolboxOpts

line = li() # 构建一个折线图对象

line.add_xaxis(["中国", "美国", "倭寇"]) # x轴
line.add_yaxis("GDP",[30,20,0.1]) # y轴


# 全局配置 和系列配置

# 全局配置 set_global_opts方法
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)



line.render()