import numpy as np
import pandas as pd
s = pd.Series([12,25,np.nan,None,pd.NA])
df = pd.DataFrame([[1,pd.NA,2],[2,3,5],[None,4,6]],columns=["第1列","第2列","第3列"])
print(s)
#缺失值的检测（查看是否为缺失值）
print(s.isna())
print(s.isnull())#null是缺失与空的意思
print(df)
print(df.isna())
print(df.isnull())#两者使用方法是一致的
print(df.isna().sum(axis=1))#注意axis=1代表的是1维，因此会根据行数播报缺失值的数目
print(s.isna().sum())
#如何剔除缺失值
print("-"*30)#分割线的用法
print(s.dropna())#一种简单的方式
print(df)
print(df.dropna())#可以很清楚地发现这是把整行都删除了
print("-"*30)
print(df.dropna(how="all"))#当全部是缺失值时，删除这一行
print(df)
print("-"*30)
print(df.dropna(thresh=3))#如果至少有2个值不是缺失值，就保留
#上面为删除一整行的
print(df.dropna(axis=1))#剔除列
#总结求和时：axis=0(竖着加);axis=1(横着加)
#删除时：axis=0(删行)；axis=1(删列)
print("-"*30)
print(df.dropna(subset=["第1列"]))#指定某一列去除，如果有缺失值就去掉缺失值所在的某一行
print(df)
print("-"*30)

#如何填充缺失值
df = pd.read_csv("data(天气).csv", encoding="gbk")
print("-"*30)
print(df.tail())
print(df.isna().sum())
#怎么填充
print(df.fillna({"temperature":20}))#fill后面跟着一个字典
#使用字典来填充（第1种）
print("-"*30)

#使用平均值填充（第2种）
print(df.fillna(df[["temperature"]].mean()))

#使用附近的值填充上(第3种，准确性相对更高)
print(df.ffill)#front，即用前面的值进行填充
print(df.bfill)#behind,即用后面的值进行填充
#注意，不同的应用场景会有不同插值的方式
