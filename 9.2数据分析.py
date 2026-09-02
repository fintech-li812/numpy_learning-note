import pandas as pd
import random

data = {
    '日期': pd.date_range(start='2024-01-01', periods=100),
    '产品': [random.choice(['手机', '电脑', '平板', '耳机']) for _ in range(100)],
    '销量': [random.randint(1, 50) for _ in range(100)],
    '销售额': [random.randint(1000, 20000) for _ in range(100)]
}

df = pd.DataFrame(data)
df.to_csv('sales_data.csv', index=False, encoding='utf-8-sig')

print("✅ 文件已生成！")
print(df.head())
df= pd.read_csv("sales_data.csv")
print(df.head())
print(df.tail())
print(df.销量.mean())
#数据的导出
#记得在创立一个临时文件夹
df.to_csv("sales_newdata.csv")
#json
df1 = pd.read_json("1234.json")
print(df1.head())

#专门用来处理json数据的库
import json
with open("1234.json","r",encoding='utf-8-sig')as f:
    data = json.load(f)
print(data)
print(type(data))