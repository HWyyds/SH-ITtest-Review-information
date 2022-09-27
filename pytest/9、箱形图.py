import pandas as pd
import matplotlib.pyplot as plt
mydf=pd.read_csv('temp.csv',encoding="ANSI")
plt.boxplot(mydf['temp_value'],sym='o',whis=1.5)
plt.show()
