# -*- coding = utf-8 -*-
# @Time :2022/4/7 10:20
# @Author :彭程
# @File :week5.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt

#中文不乱码
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
# tick_label=['语文', '数学', '英语', '物理', '化学','生物']
# # 柱形的宽度
# bar_width = 0.3
# # 根据多组数据绘制柱形图
# A = plt.bar(x, y1, tick_label=['语文', '数学', '英语', '物理', '化学','生物'], width=bar_width)
# B = plt.bar(x + bar_width, y2, width=bar_width)
# # 设置 x 轴和 y 轴的标签
# plt.ylabel("平均成绩（分）")
# # 设置 x 轴的刻度范围
# plt.xticks(x+0.3/2,tick_label)
# # 添加标题
# plt.title("高二男生、女生的平均成绩")
# # 添加图例
# plt.legend(handles=[A,B],labels=['男生', '女生'], shadow=True, fancybox=True)
#添加注释
# def autolabel(rects):
#     """ 在每个矩形条的上方附加一个文本标签, 以显示其高度"""
#     for rect in rects:
#         height = rect.get_height()    #  获取每个矩形条的高度
#         plt.text(rect.get_x() + rect.get_width() / 2, height + 2, s='{}'.format(height),ha='center', va='bottom')
# autolabel(A)
# plt.show()

# plt.bar(x, y1, tick_label=['语文', '数学', '英语', '物理', '化学','生物'], width=bar_width)
# plt.bar(x, y2, bottom=y1, width=bar_width)
# plt.show()

# # 偏差数据
# error = [2, 1, 2.5, 2, 1.5]
# # 绘制带有误差棒的柱形图
# plt.bar(x, y1, tick_label=['语文', '数学', '英语', '物理', '化学','生物'], width=bar_width)
# plt.bar(x, y1, bottom=y1, width=bar_width, yerr=error)
# plt.show()


# data = np.array([29665, 3135.4, 4292.4, 5240.9, 5543.4, 5633.8 , 6414.5 ,9308.1,10353])
# pie_labels = np.array(['童装', '奶粉辅食', '孕妈专区', '洗护喂养', '宝宝尿裤', '春夏新品' , '童车童床' , '玩具文娱' , '童鞋'])
# # 绘制饼图:半径为 0.5,数值保留1位小数
# plt.pie(data, radius=1.5, labels=pie_labels, autopct='%3.1f%%')
# plt.title("拼多多平台子类目的销售额",)
# plt.show()

data = np.array([29665, 3135.4, 4292.4, 5240.9, 5543.4, 5633.8 , 6414.5 ,9308.1,10353])
pie_labels = np.array(['童装', '奶粉辅食', '孕妈专区', '洗护喂养', '宝宝尿裤', '春夏新品' , '童车童床' , '玩具文娱' , '童鞋'])
tick_label=['童装', '奶粉服饰', '孕妈专区', '洗胃护养', '宝宝尿裤', '春夏新品','童车童床','玩具文娱','童鞋']
# 柱形的宽度
bar_width = 0.5
x = np.arange(9)
y = data
A = plt.bar(x, y, tick_label=['童装', '奶粉服饰', '孕妈专区', '洗胃护养', '宝宝尿裤', '春夏新品','童车童床','玩具文娱','童鞋'], width=bar_width,color=['r','g','b'])
plt.title("拼多多平台子类目的销售额")
plt.legend(handles=A,labels=['童装', '奶粉服饰'], loc="right",fontsize=10,shadow=False, fancybox=True)
plt.table(cellText=[y], cellLoc='center', rowLabels=['销量'],colLabels=tick_label, loc='upper center')
# colWidths=[0.1] * 3
plt.show()

