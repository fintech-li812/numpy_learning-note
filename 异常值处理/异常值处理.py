#异常值处理
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("house_data.csv")
print(df.tail())
print("-"*30)
#运用布尔索引
import pandas as pd
df = pd.read_csv("house_data.csv")
area = df.iloc[:, 3]
print(((area >= 50) & (area <= 300)).sum())

#房屋售价的异常处理
Q1 = df["价格(万元)"].quantile(0.25)
Q3 = df["价格(万元)"].quantile(0.75)
IQR = Q3 - Q1
print(IQR)
low_price = Q1 - 1.5*IQR
print(low_price)
high_price = Q3 + 1.5*IQR
print(high_price)
df = df[(df["价格(万元)"]<high_price)&(df["价格(万元)"]>low_price)]
print(df)

