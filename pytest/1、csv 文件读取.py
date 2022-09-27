import pandas as pd                                 #导入pandas库
df=pd.read_csv('test.csv',sep=',',encoding='ANSI')  #从当前目录读取test.csv文件内容放置对象df中
print(df)                                           #输出对象df中的内容
d=df["bike_id"]                                     #从对象df中调用“bike_id”字段的值放入对象d中
print(d)                                            #输出对象d中的内容
x=len(d)                                            #求对象d的长度（即包含内容的个数）放入变量x
print(x)                                            #输出变量x的值
