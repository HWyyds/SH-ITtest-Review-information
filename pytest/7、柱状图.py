import pandas as pd 
import matplotlib.pyplot as plt
mydf=pd.read_csv('bar.csv',encoding='ANSI')
plt.rcParams['font.sans-serif']=['SimHei']
plt.tick_params(labelsize=10,color='r')               #坐标轴刻度的字号
plt.title('7-10月某区图书馆站点共享单车租赁情况')
plt.xlabel('月份')
plt.ylabel('总计')
plt.bar(mydf['month'],mydf['count'],color="b")    #绘制柱状图
plt.xticks([7,8,9,10])
plt.show()
