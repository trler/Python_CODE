# 1.掌握构建一个基础的柱状图并能够反转x和y轴
from pyecharts.charts import Bar,Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *

#
bar1 = Bar()
bar2 = Bar()
bar3 = Bar()

bar1.add_xaxis(["中国", "美国", "英国"])
bar2.add_xaxis(["中国", "美国", "英国"])
bar3.add_xaxis(["中国", "美国", "英国"])

bar1.add_yaxis("GDP", [30,20,10],label_opts=LabelOpts(is_show=True,position="right"))
bar2.add_yaxis("GDP", [50,0.2,1],label_opts=LabelOpts(is_show=True,position="right"))
bar3.add_yaxis("GDP", [99,2,3],label_opts=LabelOpts(is_show=True,position="right"))

# 反转xy
bar1.reversal_axis()
bar2.reversal_axis()
bar3.reversal_axis()

# 添加时间线
time = Timeline({"theme":ThemeType.LIGHT}) # 传入字典 主题 设计颜色
time.add(bar1,"点1")
time.add(bar2,"点2")
time.add(bar3,"点3")

# 添加自动播放
time.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
)

# 绘图用时间线对象绘制

time.render("柱状图时间线.html")

