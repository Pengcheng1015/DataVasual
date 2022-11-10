# -*- coding = utf-8 -*-
# @Time :2022/4/28 10:15
# @Author :彭程
# @File :week8.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y1, y2 = np.sin(x), np.cos(x)
fig=plt.figure()
ax_one = plt.subplot(233)
ax_one.plot(x,y1,  color='#FF0000',linestyle='--', linewidth=1.0,label='cos',alpha=0.5)
ax_two = plt.subplot(236, sharex = ax_one)
ax_two.plot(x,y2, color='#0000FF', linestyle='-', linewidth=1.0, label='sin')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y1, y2 = np.sin(x), np.cos(x)
# 创建画布和布局
fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(3,4)
ax_one = fig.add_subplot(gs[0,:])
ax_two = fig.add_subplot(gs[1,0:2])
ax_thr = fig.add_subplot(gs[1,2:4])
ax_thr.plot(x,y1,  color='#FF0000',linestyle='-', linewidth=1.0,label='cos',alpha=0.5)
ax_fou = fig.add_subplot(gs[2,0])
ax_fiv = fig.add_subplot(gs[2,1:4])
ax_fiv.plot(x,y2, color='#0000FF', linestyle='-', linewidth=1.0, label='sin')
plt.show()
