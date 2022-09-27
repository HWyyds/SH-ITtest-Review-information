import pandas as pd
import matplotlib.pyplot as plt
mydf=pd.read_csv('pie.csv',encoding="ANSI")
plt.rcParams['font.sans-serif']=['SimHei']
plt.title('共享单车四季租赁情况')
labels=('春季','夏季','秋季','冬季')
plt.pie(mydf['count'],labels=labels,explode=[0, 0.1, 0, 0],autopct='%1.1f%%')
plt.show()
