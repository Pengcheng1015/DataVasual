# -*- coding = utf-8 -*-
# @Time :2022/6/2 9:38
# @Author :彭程
# @File :week11.py
# @Software: PyCharm

import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 消费收入与支出数据
flows = [-2000, -5000, -4000, -1000, -500, 20000, -500, -200]
# 流的标签列表
labels = ["旅行", "深造", "生活", "购物", "聚餐", "收入", "人气往来", "其他"]
# 流的方向
orientations = [1, 1, 1, 1, -1, -1, 0, -1]
# 创建 Sankey 类对象
sankey = Sankey()
# 为桑基图添加数据
sankey.add(flows=flows,                     # 收入与支出数据
           labels=labels,                   # 数据标签
           orientations=orientations,       # 标签显示的方向
           color="black",                   # 边缘线条颜色
           fc="lightgreen",                 # 填充颜色
           patchlabel="小兰生活收支",          # 图表中心的标签
           alpha=0.7)                       # 透明度
# 桑基图绘制完成的对象
diagrams = sankey.finish()
diagrams[0].texts[5].set_color("r")         # 将下标为 4 的数据标签设为红色
diagrams[0].texts[5].set_weight("bold")     # 将下标为 4 的数据标签设为字体加粗
diagrams[0].text.set_fontsize(20)           # 将中心标签的字体大小设为20
diagrams[0].text.set_fontweight("bold")     # 将中心标签的字体设为加粗
plt.title("小兰月生活收支的桑基图")
plt.show()