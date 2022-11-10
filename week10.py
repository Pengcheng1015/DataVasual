# -*- coding = utf-8 -*-
# @Time :2022/5/26 10:00
# @Author :彭程
# @File :week10.py
# @Software: PyCharm

# 根据数据绘制一个折线图，具体要求如下：
# 1、在距画布顶部0.2,、左侧0.2的位置上添加一个宽度为0.5、高度为0.5的绘图区域
# 2、x轴的刻度标签为周日期
# 3、刻度线样式调整：方向朝内，宽度为2
# 4、隐藏坐标轴的上、右轴脊。

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

ax = plt.axes((0.2,0.2,0.5,0.5))

x_month = np.array(['周一','周二','周三','周四','周五','周六','周日'])
y_sales = np.array([44.98,45.02,44.32,41.05,42.08,0,0])
ax.plot(x_month,y_sales)

ax.set_title('某股票一周的收盘价')
ax.set_ylabel('收盘价(元)')
ax.set_xlabel('周日期')

plt.tick_params(direction='in',width=2)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')


plt.show()
