import pandas as pd
import numpy as np
df = pd.DataFrame (
    {
        "id":[1,2,3,4,5],
        "name":["Tom","Jack","Alice","Bob","Charlie"],
        "age":[21,22,23,24,25],
        "scores":[60.5,80,30.6,70,83.5]
    },index=[1,2,3,4,5],columns=["name","age","scores"])
print("行索引:")
print(df.index)
print("列标签：")
print(df.columns)
print("值：")
print(df.values)
print("维度：",df.ndim)
print("数据类型:",df.dtypes)
print("形状：",df.shape)
print("元素个数：",df.size)
print(df.T.index)
print(df.T)#从形状开始变化
#获取元素 loc,iloc,at,iat
#某行
print(df.loc[4])
#获取某列数据
print(df.loc[ :,"name"])
#获取单个具体的数据
print(df.at[1,"name"])#显式
print(df.iloc[1:0])#隐式
