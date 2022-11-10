# -*- coding = utf-8 -*-
# @Time :2022/4/14 10:00
# @Author :彭程
# @File :week6.py
# @Software: PyCharm

#week6 第一题
import matplotlib
from jupyterthemes import jtplot
import numpy as np
import matplotlib.pyplot as plt
jtplot.style()

#中文不乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# x = np.arange(1, 13,1)
# y_max = np.array([39, 20, 40, 38, 42, 43, 41, 41, 45, 48, 52, 50])
# y_min = np.array([45, 28, 48, 49, 50, 51, 50, 50, 51, 52, 70, 65])
# # 绘制折线图
#
# plt.plot(x, y_max, 'r^:', label='2018年', linewidth=1.5)
# plt.plot(x, y_min, 'bD-', label='2019年', linewidth=1.5)
# plt.xlabel('月份',fontsize=10)
# plt.ylabel("业务量(亿件",fontsize=10)
# plt.xticks(np.arange(1, 13, 1))
# plt.grid()
# plt.legend()
# plt.style.use("fivethirtyeight")
# plt.show()

#week6 第二题
from jupyterthemes import jtplot
import numpy as np
import matplotlib.pyplot as plt
matplotlib.matplotlib_fname()
#中文不乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1, 'r:', label='Sin', linewidth=1.0)
plt.plot(x,y2, 'b-',label='Cos',linewidth=1.0,alpha=0.5)
#图例
plt.legend()
# 设置 x 轴和 y 轴的标签
plt.xlabel("x")
plt.ylabel("y")
# 设置标题
plt.title("cos & sin")
# 设置 x 轴，y轴的刻度范围和刻度标签
plt.xlim(x.min() * 1.5, x.max()  * 1.5)
plt.xticks([-np.pi,-np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
plt.yticks([-1.0,-0.5,0.0,0.5,1.0])
# 添加指向型注释文本
plt.annotate("cos(t)",
             xy=(1.0, np.cos(1)),
             xytext=(np.pi/2, 1.0),
             arrowprops=dict(arrowstyle="->"))
# 添加无指向型注释文本
plt.text(np.pi, -1.1, "BY 彭程", bbox=dict(alpha=0.2))
#填充区域 (|x|<0.5 or cosx>0.5)
plt.fill_between(x,y2,1,where=(abs(x)<0.5) ,color='green', alpha=0.25)
plt.fill_between(x,y2,0,where=(y2>0.5),color='green',alpha=0.25)
plt.fill_between(x,y2,0,where=(abs(x)<0.5),color='white',alpha=0.25)
plt.show()
