import pandas as pd                        #导入pandas库
df=pd.read_csv("test.csv",encoding="ANSI") #从当前目录读取test.csv文件内容放置对象df中
print(df)         # 输出修改前的内容
df.drop_duplicates(subset=['bike_id','datetime'],keep='first',inplace=True)     #对df对象中“bike_id”，“datetime”字段的值相同的记录保留第一条，在原表上进行修改。
print(df)         # 输出修改后的内容
df.to_csv("testqc.csv",encoding="ANSI")    #将修改后的df保存到testqc.cvs文件中
