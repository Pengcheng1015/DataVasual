# -*- coding = utf-8 -*-
# @Time :2022/4/22 15:49
# @Author :彭程
# @File :week7.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import scipy.stats as sci


crime = pd.read_csv("crimeRatesByState2005.csv")
crime2 = crime[crime.state != "United States"]
crime2 = crime2[crime2.state != "District of Columbia"]
j = sns.jointplot(x='murder', y='burglary', data=crime2, kind='reg', height=7, ratio=3, color='g', ylim=(0, 1600),
                  xlim=(0, 12.5))
r, p = sci.pearsonr(crime2.murder, crime2.burglary)
phantom, = j.ax_joint.plot([], [], linestyle="", alpha=0)
j.ax_joint.legend([phantom], ['pearsonr={:.2f},p={:.2e}'.format(r, p)])
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
crime = pd.read_csv("crimeRatesByState2005.csv")
crime2 = crime[crime.state != "United States"]
crime2 = crime2[crime2.state != "District of Columbia"]
crime2=crime2.drop(['state'],axis=1)
g=sns.pairplot(crime2)
plt.show()