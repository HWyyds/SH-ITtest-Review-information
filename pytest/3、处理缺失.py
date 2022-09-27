import pandas as pd     #导入pandas库
df=pd.read_csv("test.csv",encoding="ANSI")    #从当前目录读取test.csv文件内容放置对象df中
print(df)     # 输出修改前的内容
df.dropna(axis=0,inplace=True)  #以行为单位，将每条记录中有空白的记录删除
print(df)       # 输出修改后的内容
df.to_csv("testqs.csv",encoding="ANSI")      #将修改后的df保存到testqs.cvs文件中
