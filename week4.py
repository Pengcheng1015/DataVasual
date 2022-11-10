# -*- coding = utf-8 -*-
# @Time :2022/3/24 10:59
# @Author :彭程
# @File :week4.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# x = np.arange(6)
# y1 = np.array([85.5, 91, 72, 59, 66 ,55])
# # 柱形的宽度
# bar_width = 0.3
# # 绘制柱形图
# plt.bar(x, y1, tick_label=['语文', '数学', '英语', '物理', '化学','生物'], width=bar_width)
# plt.show()

# x = np.arange(6)
# y1 = np.array([85.5, 91, 72, 59, 66 ,55])
# y2 = np.array([94, 82, 89.5, 62, 49, 53])
#  柱形的宽度
# bar_width = 0.3
# 根据多组数据绘制柱形图
# plt.bar(x, y1, tick_label=['语文', '数学', '英语', '物理', '化学','生物'], width=bar_width)
# plt.bar(x + bar_width, y2, width=bar_width)
# plt.show()

# plt.bar(x, y1, tick_label=['语文', '数学', '英语', '物理', '化学','生物'], width=bar_width)
# plt.bar(x, y2, bottom=y1, width=bar_width)
# plt.show()

 # 偏差数据
# error = [2, 1, 2.5, 2, 1.5]
 # 绘制带有误差棒的柱形图
# plt.bar(x, y1, tick_label=['语文', '数学', '英语', '物理', '化学','生物'], width=bar_width)
# plt.bar(x, y1, bottom=y1, width=bar_width, yerr=error)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
data = np.array([29665, 3135.4, 4292.4, 5240.9, 5543.4, 5633.8 , 6414.5 ,9308.1,10353])
pie_labels = np.array(['童装', '奶粉辅食', '孕妈专区', '洗护喂养', '宝宝尿裤', '春夏新品' , '童车童床' , '玩具文娱' , '童鞋'])
# 绘制饼图:半径为 0.5,数值保留1位小数
plt.pie(data, radius=1.5, labels=pie_labels, autopct='%3.1f%%')
plt.show()

