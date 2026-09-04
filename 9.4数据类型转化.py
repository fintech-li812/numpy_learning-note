import numpy as np
import pandas as pd
data = {
    "name":["alice","alice","bob","alice","jack","bob"],
    "age":[26,25,30,25,35,30],
    "city":["NY","NY","LA","NY","SF","LA"]
}
df = pd.DataFrame(data)
print(df)
print("-"*30)

#先检查是否重复
print(df.duplicated())#会找出完全重复的，整个的一条记录，会被返回为True
print("-"*30)

#再看用drop删除
print(df.drop_duplicates(subset=["city"]))#查看不重复的，subset是根据某一列去重
print("-"*30)

df.drop_duplicates(subset=["name"],keep="last")#会保存最新出现的，keep在这里是保存的意思
#数据类型的转换
print("-"*30)

df = pd.read_csv("data(天气).csv",encoding="gbk")
print(df.dtypes)#object一般指的是字符串
print("-"*30)
#某些数据类型可以进行优化
df["id"] = df["id"].astype("int16")#astype上进行类型转换
print(df.dtypes)
print("-"*30)

#有字符串的可以进行一个分类
df["weather"] = df["weather"].astype("category")
print(df.dtypes)
print(df.weather)
print(df.weather.nunique())#此处统计的是多少不重复的类型
print("-"*30)

#可以判断是否为具体的某一类型（判断函数）
df["is_多云"] = df["weather"].map({"多云":True,}).fillna(False)
print(df.is_多云)#把现在的值全部变为布尔值
print("-"*30)



