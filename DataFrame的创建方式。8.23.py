import numpy as np
import pandas as pd
#利用Series来创建
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([6,7,8,9,10])
df = pd.DataFrame({"第一列":s1,"第二列":s2})
print(df)
print(type(df))#每一列都是一个Series
#通过字典来创建
df = pd.DataFrame (
    {
        "id":[1,2,3,4,5],
        "name":["Tom","Jack","Alice","Bob","Charlie"],
        "age":[21,22,23,24,25],
        "scores":[60.5,80,30.6,70,83.5]#强制转换优先级：bool<int<<floet<str
    },index=[1,2,3,4,5],columns=["name","age","scores"]#用来调整顺序
)#用字典的方式创建
print(df)