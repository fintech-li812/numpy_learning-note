import pandas as pd
df = pd.read_csv("sales_data.csv")
print(df.head(10))
print("-"*30)
df1 = df.head(10)[["销售数量","单价","销售区域"]]#(两个中括号号里面的内容什幺八七复制过来的内容)
print(df1)

#进行分箱的操作
print("-"*30)
print(pd.cut(df1["单价"],bins=2).value_counts())#分成了n段区间,起始值与结束值都是所有数据
print("-"*30)
df1["价格高低"]=pd.cut(df1["单价"],bins=[0,1000,8000],labels=["低","高"])
print(df1)
print("-"*30)
print(pd.qcut(df1["销售数量"],3).value_counts())#这里是等频率去分
print(df1)
print("-"*30)
df1["销售区域"]=df1["销售区域"].astype("category")
print(df1)
print("-"*30)
#df.rename()    df.set_index()      df.reset_index()
df = pd.DataFrame({
    "name":["Jack","alice","tom","bob"],
    "age":[20,30,40,50],
    "gender":["male","female","male","female"]
})
df.set_index("name",inplace=True)
print(df)
df.rename(columns={"age":"年龄"},inplace=True)
print(df)
print("-"*30)




