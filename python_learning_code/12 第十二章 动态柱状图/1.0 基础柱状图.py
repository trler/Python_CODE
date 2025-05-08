# 1.掌握构建一个基础的柱状图并能够反转x和y轴
from pyecharts.charts import Bar
from pyecharts.options import *

#
bar = Bar()

bar.add_xaxis(["中国", "美国", "英国"])

bar.add_yaxis("GDP", [30,20, 10],label_opts=LabelOpts(is_show=True,position="right"))

# 反转xy
bar.reversal_axis()

bar.render("柱状图.html")

