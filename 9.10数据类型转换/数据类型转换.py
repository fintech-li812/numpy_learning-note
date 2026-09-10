import pandas as pd
import numpy as np
df = pd.read_csv("销售数据.csv")
print(df.head())


#检查是否有缺失值
df.isna().sum()
#删除缺失值
df.dropna().sum()

#检查是否有重复值
df.duplicated().sum()
#删除重复值
df.drop_duplicates(inplace=True)

#进行数据转换
df["销售额"] = df["销售额"].astype(str) + "元"
print(df)#注意只有字符串可以拼接
#怎么去单位
#df["列名"] = df["列名“].str.replace("","").astype(float/int),astypr不用加引号
print("-"*30)


#区域的数据类型构造
df["区域"] = df["区域"].astype("category")
print(df["区域"].dtypes)

#总结：先用.str转换成字符串，再用astype转换成另一种类型