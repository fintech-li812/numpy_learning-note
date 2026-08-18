import pandas as pd
import numpy as np
s = pd.Series([10,2,np.nan,None,3,4,5],index= ["A","B","C","D","E","F","G"],name = "Data")
print(s)
print(s.head()) #默认取前五行数据
print(s.tail(2))#默认取后五行数据
#查看描述性讯息
print(s.describe())
print(s.var())#方差
#获取元素个数
print(s.nunique())
print(s.count())
#获取索引
print(s.keys() )#方法，带小括号
print(s.index)#属性
print(s.isna())#检查是否为缺失值
print(s.isin([4,5,6]))#看值是否在s里面，并确定位置
print(s.sort_values())#排序
print(s.quantile(0.25))
print(s.quantile(0.8))
#众数
print (s.mode())
#频率
print(s.value_counts())#左值，右频率
#去重
print(s.drop_duplicates)
#unique是去重，nunique是个数
#索引排序
print(s.sort_index())
#值排序
print(s.sort_values())


