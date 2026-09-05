#数据变形
import pandas as pd
import numpy as np
data = {"ID":[1,2],
        "name":["alice","bob"],
    "math":[90,85],
    "English":[88,92],
    "Science":[95,89]
}
df = pd.DataFrame(data)
print(df)
#这样打印出来的叫做宽表
print("-"*30)
df.T
print(df)
#如何变成  1  alice   math   90
#        1   alice  English 88
print("-"*30)
#要对当前的进行变形
#宽表转换成长表
df2 = pd.melt(df,id_vars=["ID","name"],var_name = "科目",value_name = "分数")#vars里传的是不改的，把后面列的名字当作变量
print(df2)
print("-"*30)
df2.sort_values("name")#sort_value是根据某个值来排序(这里是根据name来排序的)
print(df2)
print("-"*30)
#长表转宽表（原理一样但是语句不同）
print(pd.pivot(df2,index = ["ID","name"],columns = "科目",values = "分数"))#也可以反过来写
print("-"*30)
data2 = {"ID":[1,2],
        "name":["alice Smith","bob Smith"],
    "math":[90,85],
    "English":[88,92],
    "Science":[95,89]
}
#分列
#提出问题，怎么将姓和名分开，让粒度更细
df = pd.DataFrame(data2)
print("-"*30)
df[["first","last"]]=df["name"].str.split(" ",expand=True)#重点是将它当作字符串，再用字符串的方式将它分隔开,用expand将其变成DataFrame的格式，这里是将空格作为一个字符串
print(df)
print("-"*30)
#str作为字符串的选择器，所以理论上也可以将任何关于字符串的操作都用上
#复习转换，df["high"]=df["high"].astype("int64")
#可以将天气的最高与最低设置为字符串，再分别统计其平均分