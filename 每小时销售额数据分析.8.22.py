import numpy as np
import pandas as pd
np.random.seed(42)
hour_sales = pd.Series(np.random.randint(0,100,24),
          index =pd.date_range("2025-01-01",periods= 24,freq = "h") )
print(hour_sales)
#按天重采样计算总销售额
#day_sales=hour_sales.resample("D").sum()
#print(hour_sales.resample("D").sum())
day_sales = hour_sales.sum()
#计算每天营业时间与非营业时间的销售额比例
#business_hour_sales = hour_sales.between_time("8:00","22:00")#筛选一段时间内的方式
#布尔索引
business_hour_sales  =  hour_sales[(hour_sales.index.hour>=8)&(hour_sales.index.hour<=22)]
print(business_hour_sales)
print(business_hour_sales.sum()/(day_sales -business_hour_sales.sum()))
#非营业时间：n_b = h.drop(b.yandex)
#n_b = h[(h.index.hour<8) | (h.index.hour<22)
#项目中要见名知意
print(business_hour_sales.nlargest(3))#取出最大的3个元素
print(business_hour_sales.nlargest(3).keys())#取索引