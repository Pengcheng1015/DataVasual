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

tick_label=['����', '��ѧ', 'Ӣ��', '����', '��ѧ','����']

def zhu(x,y1,y2):
    zhu1 = plt.bar(x, y1, tick_label=['����', '��ѧ', 'Ӣ��', '����', '��ѧ','���'],width=0.3)
    zhu2 = plt.bar(x + 0.3, y2, width=0.3)
    plt.xticks(x+0.3/2, tick_label)     #ΪX���趨��ǩ
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()    #  ��ȡÿ���������ĸ߶�
            plt.text(rect.get_x() + rect.get_width( ) / 2, height + 3, s='{}'.format(height))
    autolabel(zhu1)
    autolabel(zhu2)
    plt.legend(handles=[zhu1,zhu2],labels=["����","Ů��"],loc="upper right",fontsize=10)
    plt.show()

zhu(x,y1,y2)

def bing(X,tick_label):
    fig = plt.figure()
    plt.pie(X, labels=tick_label, autopct='%1.2f%%')
    plt.title("�������Ƴɼ���ͼ�ֲ�")
    plt.show()

bing(y1,tick_label)



def reli(x_ticks,y_ticks):        #��ɫԽ���������ֶ���Խ��
    values = np.random.rand(6, 6)
    ax = sns.heatmap(values, xticklabels=x_ticks, yticklabels=y_ticks)
    ax.set_title('��Ů���ɼ������ֲ�ͼ')  # ͼ����
    ax.set_xlabel('��')  # x�����
    ax.set_ylabel('Ů')
    plt.show()

reli(y1,y2)



def zhifang(y1,lable):
    plt.hist(x=lable,  # ָ����ͼ����

    bins = 6,  # ָ��ֱ��ͼ������ĸ���

    color = 'steelblue',  # ָ��ֱ��ͼ�����ɫ

    edgecolor = 'black'  # ָ��ֱ��ͼ�ı߿�ɫ
              )
      # ���x���y���ǩ
    plt.bar(x, y1, align='center')
    plt.xlabel('ѧ��')

    plt.ylabel('����')
     # ��ӱ���

    plt.title('�����ɼ��ֲ�')
    # ��ʾͼ��

    plt.show()

zhifang(y1,tick_label)

def mianji(lable,y):
    # Area plot
    # ���ƻ������ͼ
    plt.fill_between(lable, y)

    plt.title('Ů�����ͼ�ֲ�')
    plt.show()

mianji(tick_label,y2)

def denggaoxian(x,y):
    X, Y = np.meshgrid(x, y)
    # д�뺯����z�Ǵ�д
    Z = X ** 2 + Y ** 2
    # ���ô򿪻�����С,��10����6
    # plt.figure(figsize=(10,6))
    # �����ɫ��f��filled
    plt.contourf(X, Y, Z)
    # ���ȸ���
    plt.contour(X, Y, Z)
    plt.title('��Ů���ɼ��ȸ���ͼ')
    plt.show()


denggaoxian(y1,y2)


def zhexian(lable,y1,y2):
    plt.title('��Ů���ɼ�����ͼ�ֲ�')
    zhexian1, = plt.plot(lable, y1)
    zhexian2, = plt.plot(lable, y2)
    plt.legend(handles=[zhexian1, zhexian2], labels=["����", "Ů��"], loc="upper right", fontsize=10)
    plt.show()

zhexian(tick_label,y1,y2)


def leida(values2,feature):

    # ����ÿ�����ݵ����ʾλ�ã����״�ͼ���ýǶȱ�ʾ
    angles = np.linspace(0, 2 * np.pi, len(feature), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))
    feature = np.concatenate((feature, [feature[0]]))
    # ��ͼ
    fig = plt.figure()
    for values in [values2]:
        # ƴ��������β��ʹͼ�����������
        values = np.concatenate((values, [values[0]]))
        # ����Ϊ�������ʽ
        ax = fig.add_subplot(111, polar=True)
        # ��������ͼ
        ax.plot(angles, values, 'o-', linewidth=2)
        # �����ɫ
        ax.fill(angles, values, alpha=0.25)

        # ����ͼ���ϵĽǶȻ��̶ֿȣ�Ϊÿ�����ݵ㴦��ӱ�ǩ
        ax.set_thetagrids(angles * 180 / np.pi, feature)

        # �����״�ͼ�ķ�Χ
        ax.set_ylim(40, 100)

    # ��ӱ���
    plt.title('Ů���ɼ��״�ֲ�ͼ')
    # ���������
    ax.grid(True)

    plt.show()

leida(y2,tick_label)

def midu(y1):
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    from scipy import stats

    # ���seed(),����ȷ��һ���������
    ## ������滹��Ҫ�õ������������
    ## ���Ա��ֲ���һ������ִ��һ�Σ���������������������һ�µġ�
    # rn1 �����ɵ�һ��meanΪ 0 ��SDΪ 1 ����̬�ֲ�������
    np.random.seed(520)


    # ʹ��ggplot����ʽ
    plt.style.use('ggplot')

    # ��������ĺ��Ĵ��룬seaborn.distplot()���ڻ���ֱ��ͼ�������ܶ�/���ܶ����ߡ�������ߡ�
    ## ���� rn1 ���������ݣ���һ��list��һ��np��narray����
    ## hist=True/False���Ƿ����ֱ��ͼ���������hist_kws={}��������ϸ���ã����������ڣ���׸����
    ## kde=True/False���Ƿ���ƺ��ܶ����ߣ��������kde_kws={},������ϸ���ã�ʵ��ʹ��ʱ�������ܶ����߳�ʹ��������߱�ʾ����׸����
    ## fit=stats.norm�����ģ�ͣ�һ������̬�ֲ���norm/stats.norm�����ԣ��������fit_kws={}������Ϣ���ã�
    ### fit_kws={'color':'���������ɫ','label':'ͼ��˵��','linestyle':'������ʽ'}
    sns.distplot(y1, hist=False, kde=False, fit=stats.norm,
                 fit_kws={'color': 'black', 'label': 'u=0,s=1', 'linestyle': '-'})

    # legend()��ʾͼ����savefig()����ͼƬ��show()��ͼ
    plt.legend()
    plt.title('�����ɼ������ܶ�')
    plt.show()
midu(y1)


def huafubing(lable,y1):

    plt.figure(
        FigureClass =Waffle,
        rows=5,
        columns=10,
        values=y1,
        # ����ͼ����λ��
        legend={'labels': lable,
        'loc': 'upper left',
        'bbox_to_anchor': (1, 1)
    },
        dpi=100
    )
    plt.title('�����ɼ������ͼ')
    plt.show()

huafubing(tick_label,y1)



