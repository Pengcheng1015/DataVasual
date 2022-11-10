# -*- coding = utf-8 -*-
# @Time :2022/5/12 15:23
# @Author :彭程
# @File :week9.py
# @Software: PyCharm

import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from imageio import imread
text =open('tangshi.txt','r').read()

cut_text = jieba.cut(text)

result = " ".join(cut_text)
bg_pic = imread('week9.png')

wc = WordCloud(
    #设置字体
    font_path=r'.\simhei.ttf',
    #设置背景色
    background_color='white',
    #设置背景宽
    width=500,
    #设置背景高
    height=350,
    #最大字体
    max_font_size=50,
    #最小字体
    min_font_size=20,
    mask=bg_pic
)
#产生词云
wc.generate(result)
#保存图片
wc.to_file(r"wordcloud.png")
#显示图片
#指定所绘图名称
plt.figure("jay")
#以图片的形式显示词云
plt.imshow(wc)
#关闭图像坐标系
plt.axis("off")
plt.show()