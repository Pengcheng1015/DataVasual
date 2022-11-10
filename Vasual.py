# -*- coding: gbk -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pywaffle import Waffle

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(6)
y1 = np.array([85.5,91,72,59,66,55])
y2 = np.array([94,82,89.5,62,49,53])

tick_label=['语文', '数学', '英语', '物理', '化学','生物']

def zhu(x,y1,y2):
    zhu1 = plt.bar(x, y1, tick_label=['语文', '数学', '英语', '物理', '化学','生物·'],width=0.3)
    zhu2 = plt.bar(x + 0.3, y2, width=0.3)
    plt.xticks(x+0.3/2, tick_label)     #为X轴设定标签
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()    #  获取每个矩形条的高度
            plt.text(rect.get_x() + rect.get_width( ) / 2, height + 3, s='{}'.format(height))
    autolabel(zhu1)
    autolabel(zhu2)
    plt.legend(handles=[zhu1,zhu2],labels=["男生","女生"],loc="upper right",fontsize=10)
    plt.show()

zhu(x,y1,y2)

def bing(X,tick_label):
    fig = plt.figure()
    plt.pie(X, labels=tick_label, autopct='%1.2f%%')
    plt.title("男生各科成绩饼图分布")
    plt.show()

bing(y1,tick_label)



def reli(x_ticks,y_ticks):        #颜色越深代表这个分段人越多
    values = np.random.rand(6, 6)
    ax = sns.heatmap(values, xticklabels=x_ticks, yticklabels=y_ticks)
    ax.set_title('男女生成绩热力分布图')  # 图标题
    ax.set_xlabel('男')  # x轴标题
    ax.set_ylabel('女')
    plt.show()

reli(y1,y2)



def zhifang(y1,lable):
    plt.hist(x=lable,  # 指定绘图数据

    bins = 6,  # 指定直方图中条块的个数

    color = 'steelblue',  # 指定直方图的填充色

    edgecolor = 'black'  # 指定直方图的边框色
              )
      # 添加x轴和y轴标签
    plt.bar(x, y1, align='center')
    plt.xlabel('学科')

    plt.ylabel('分数')
     # 添加标题

    plt.title('男生成绩分布')
    # 显示图形

    plt.show()

zhifang(y1,tick_label)

def mianji(lable,y):
    # Area plot
    # 绘制基础面积图
    plt.fill_between(lable, y)

    plt.title('女生面积图分布')
    plt.show()

mianji(tick_label,y2)

def denggaoxian(x,y):
    X, Y = np.meshgrid(x, y)
    # 写入函数，z是大写
    Z = X ** 2 + Y ** 2
    # 设置打开画布大小,长10，宽6
    # plt.figure(figsize=(10,6))
    # 填充颜色，f即filled
    plt.contourf(X, Y, Z)
    # 画等高线
    plt.contour(X, Y, Z)
    plt.title('男女生成绩等高线图')
    plt.show()


denggaoxian(y1,y2)


def zhexian(lable,y1,y2):
    plt.title('男女生成绩折线图分布')
    zhexian1, = plt.plot(lable, y1)
    zhexian2, = plt.plot(lable, y2)
    plt.legend(handles=[zhexian1, zhexian2], labels=["男生", "女生"], loc="upper right", fontsize=10)
    plt.show()

zhexian(tick_label,y1,y2)


def leida(values2,feature):

    # 设置每个数据点的显示位置，在雷达图上用角度表示
    angles = np.linspace(0, 2 * np.pi, len(feature), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))
    feature = np.concatenate((feature, [feature[0]]))
    # 绘图
    fig = plt.figure()
    for values in [values2]:
        # 拼接数据首尾，使图形中线条封闭
        values = np.concatenate((values, [values[0]]))
        # 设置为极坐标格式
        ax = fig.add_subplot(111, polar=True)
        # 绘制折线图
        ax.plot(angles, values, 'o-', linewidth=2)
        # 填充颜色
        ax.fill(angles, values, alpha=0.25)

        # 设置图标上的角度划分刻度，为每个数据点处添加标签
        ax.set_thetagrids(angles * 180 / np.pi, feature)

        # 设置雷达图的范围
        ax.set_ylim(40, 100)

    # 添加标题
    plt.title('女生成绩雷达分布图')
    # 添加网格线
    ax.grid(True)

    plt.show()

leida(y2,tick_label)

def midu(y1):
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    from scipy import stats

    # 这个seed(),就是确定一组随机数，
    ## 如果后面还需要用到这组随机数，
    ## 可以保持参数一致重新执行一次，后面出来的随机数数组是一致的。
    # rn1 是生成的一组mean为 0 ，SD为 1 的正态分布的数组
    np.random.seed(520)


    # 使用ggplot的样式
    plt.style.use('ggplot')

    # 本次需求的核心代码，seaborn.distplot()用于绘制直方图、概率密度/核密度曲线、拟合曲线。
    ## 其中 rn1 是输入数据，是一个list或一个np的narray对象；
    ## hist=True/False，是否绘制直方图，可以添加hist_kws={}，进行详细设置，不在需求内，不赘述；
    ## kde=True/False，是否绘制核密度曲线，可以添加kde_kws={},进行详细设置，实际使用时，概率密度曲线常使用拟合曲线表示，不赘述；
    ## fit=stats.norm，拟合模型，一般是正态分布，norm/stats.norm都可以，可以添加fit_kws={}进行消息设置，
    ### fit_kws={'color':'拟合曲线颜色','label':'图例说明','linestyle':'曲线样式'}
    sns.distplot(y1, hist=False, kde=False, fit=stats.norm,
                 fit_kws={'color': 'black', 'label': 'u=0,s=1', 'linestyle': '-'})

    # legend()显示图例，savefig()保存图片，show()绘图
    plt.legend()
    plt.title('男生成绩概率密度')
    plt.show()
midu(y1)


def huafubing(lable,y1):

    plt.figure(
        FigureClass =Waffle,
        rows=5,
        columns=10,
        values=y1,
        # 设置图例的位置
        legend={'labels': lable,
        'loc': 'upper left',
        'bbox_to_anchor': (1, 1)
    },
        dpi=100
    )
    plt.title('男生成绩华夫饼图')
    plt.show()

huafubing(tick_label,y1)



