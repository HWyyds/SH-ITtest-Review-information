import pandas as pd                     # 导入pandas库
import matplotlib.pyplot as plt         # 导入Matplotlib的pyplot子库 
plt.rcParams['font.sans-serif']=['SimHei']  #支持中文，用于正常显示中文标签
mydf=pd.read_csv('xz.csv',encoding="ANSI")  #读取xz.csv文件存入对象mydf
plt.title('莘庄共享单车站点附近一天的共享单车流量') #设置标题内容
plt.xlabel('小时')   #设置X轴标题内容
plt.ylabel('总计')   #设置Y轴标题内容
plt.scatter(mydf['hour'],mydf['total'],c='r',marker='^')   #绘制散点图（数据：x轴为mydf中['hour']字段的值,y轴为mydf中['total']字段的值
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]) #设置X轴的刻度
plt.savefig('xz-1.jpeg') #保存到xz-1.jpeg文件中
plt.show()               # 显示图表           
