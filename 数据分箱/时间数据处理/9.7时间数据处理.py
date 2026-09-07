#时间数据的处理
import  pandas as pd
d = pd.Timestamp("2015-05-02 10:22")
print(d)
print(type(d))
print("年：",d.year)#month,day,hour,minute,second
print("季度：",d.quarter)
print("是否是月底：",d.is_month_end)
print("星期几：",d.day_name)
print("转化为天：",d.to_period("Q"))#用的是英文的首字母

#字符串转换为日期类型
a = pd.to_datetime("2015-05-02 10:22")
print(a)
print(type(a))
print(a.day_name())

#dataFrame 日期转换
df = pd.DataFrame({
    "sales":[100,200,300],
    "date":["20250601","20260602","20250603"]
})
df["datetime"] = pd.to_datetime(df["date"])
print(df)
print(df.info())
print(type(df["datetime"]))
df["week"] = df["datetime"].dt.day_name()
print(df)
print(df["datetime"].dt.year)

#csv日期转换
df = pd.read_csv("data(天气).csv")
print(df.head())
print("-"*30)

#怎么将字符串转换为日期
df["datatime"] = pd.to_datetime(df["time"])
print(df.isnull().sum())
df.dropna()
print(df.info)
df["time"] = pd.to_datetime(df["time"])

print("-"*30)
df["time"] = pd.to_datetime(df["time"])
#将日期数据作为索引
df = df.set_index("time")#记住要从新进行赋值，也可以用inplace = True,将原来的索引给替换掉
print(df.index)
print(df)

#对日期进行切片,可以先删除，在排序
df = df[df.index.notna()]
df = df.sort_index()
print(df.loc["2026-08-02":"2026-08-03"])

#时间间隔
d1 = pd.Timestamp("2026-01-01")
d2 = pd.Timestamp("2026-09-08")
d3 = d2-d1
print(type(d3))
print(d3)

#更加简单的一个方式，直接在读取的时候将格式进行转换
df = pd.read_csv("sample_data.csv",parse_dates=["date"])
print(df.info())

#这是将date设置成索引
df = df.set_index("date").sort_index()

#查看索引名字
print(df.index.name)

#记得删除空行
df = df[df.index.notna()]

#排序（保证单调序列）

#计算时间差
df["delta"] = df.index - df.index[0]
print(df)
print("-"*30)

#时间切片
print(df.loc["2026-09-01":"2026-09-10"])#注意这里用的是冒号
days = pd.date_range("2026-08-02","2026-09-30",freq = "W")#注意range是用的逗号
print(days)
print("-"*30)


