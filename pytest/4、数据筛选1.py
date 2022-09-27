import numpy as np       #导入munpy库
import pandas as pd      #导入pandas库
df=pd.read_csv("test1.csv",encoding="ANSI")    #读取test1.csv中的内容放入二维表df中
mydf=df[((df['year_month']>='06-21-00')&(df['year_month']<='06-21-23') & (df['local_name']=='图书馆'))] #在df中筛选出["year_month"]字段的在（06-21-00,06-21-23）之间去，并且字段["local_name"]的值为“图书馆”的记录。
print(mydf)      #输出mydf的内容
thiscount=mydf['year_month']  #读取mydf中字段["year_month"]的值，放入对象thiscount中
print(thiscount)   #输出thiscount的内容
t=thiscount.value_counts() #统计thiscount中["year_month"]的值相同的记录，并存入变量t
print(t)  #输出t的值
