import numpy as np
import pandas as pd
sales = pd.Series([120,135,145,160,155,170,180,175,190,200,210,220],index = pd.date_range("2022-01-01",periods=12,freq = "ME"))
print(sales)#W是周
print(sales.resample("QS").mean())#重新采样
#sales.groupby(sales.index.quarter).mean
print("销量最高的月份为",sales.idxmax())
print("月环比的增长率为",sales.pct_change())
a = sales.pct_change()
b= a>0#取连续增长的月份
print(b[b.rolling(3).sum()==3].keys)#取三行进行滚动
#this_month_growth = sales.diff()>0
#last_month_growth = this_month_growth.shift(1)
#s = this_month_growth & last_month_growth
#result = sales[s]
#print(result)