# _*_ coding:utf-8 _*_
# #1.散点图(scatter plot):matplotlib
# import matplotlib.pyplot as plt
# plt.scatter(x,y,marker=None)    #marker:'x','>','o'
#
# #seaborn
# import seaborn as sns
# sns,jointplot(x,y,data=None,kind='scatter')  #下标，传入数据，图形类型

#例子：随机的1000个点
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#数据准备
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
#用Matplotlib画散点图
plt.scatter(x,y,marker='x')
plt.show()
#用seaborn画散点图
df = pd.DataFrame({'x':x,'y':y})
sns.jointplot(x='x',y='y',data=df,kind='scatter');
plt.show()

#2.折线图
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]
#使用matplotlib
plt.plot(x, y)
plt.show()
#使用seaborn
df = pd.DataFrame({'x': x, 'y': y})
sns.lineplot(x='x', y='y',data=df)
plt.show()

#3.直方图
a = np.random.randn(100)
s = pd.Series(a)
#用matplotlib
plt.hist(s)
plt.show()
#用seaborn
sns.distplot(s, kde=False)  #kde显示核密度估计
plt.show()
sns.distplot(s, kde=True)
plt.show()

#4.条形图
x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
y = [5, 4, 8, 12, 7]
#matplotlib
plt.bar(x, y)
plt.show()
#seabornn
sns.barplot(x, y)
plt.show()

#5.箱线图
#生成 0-1 之间的10*4 维度数据
data = np.random.normal(size=(10,4))
lables = ['A', 'B', 'C', 'D']
#matplotlib
plt.boxplot(data,lables=lables)
plt.show()
#seaborn
df = pd.DataFrame(data, columns=lables)
sns.boxplot(data=df)
plt.show()

#6.饼图
nums = [25, 37, 33, 37, 6]
lables = ['High-school','Bachelor', 'Master', 'Ph.d', 'Others']
#matplotlib
plt.pie(x = nums, lables=lables)
plt.show()

#7.热力图 heat map
flights = sns.load_dataset("flights")
data = flights.pivot('year', 'month', 'passengers')
#seaborn
sns.heatmap(data)
plt.show()

#8.蜘蛛图:显示一对多关系
from matplotlib.font_manager import FontProperties
lables = np.array([u" 推进 ","KDA",u" 生存 ",u" 团战 ",u" 发育 ",u" 输出 "])
stats = [83, 61, 95, 67, 76, 88]
#画图数据准备，角度，状态值
angles = np.linspace(0, 2*np.pi, len(lables), endpoint=False)
stats = np.concatenate((stats,[stats[0]]))
angles = np.concatenate((angles,angles[0]))
#用Matplotlib画蜘蛛图
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, alpha=0.25)
#设置中文字体
font = FontProperties(fname=r"-------", size=14)
ax.set_thetagrids(angles * 180/np.pi, lables, FontProperties=font)
plt.show()

#9.二元变量分布
tips = sns.load_dataset("tips")
print(tips.head(10))
#用seaborn画二元变量分布图（散点图，核密度图，Hexbin图）
sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter")
sns.jointplot(x="total_bill", y="tip", data=tips, kind="kde")
sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
plt.show()
