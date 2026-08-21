import pandas as pd
import numpy as np
prices = pd.Series([102.3,103.5,105.1,104.8,106.2,107.0,106.5,108.1,109.3,110.2],index = pd.date_range("2023-01-01",periods=10))
print(prices)
#date = pd.date_range("2023-01-01",periods=6)
#print(list(date))
print(prices.pct_change())
#等效于pries.diff()/pries.shift(1)
a = prices.pct_change()
print(a.max())
#取日期
print(a.idxmax())#最小值计算同理
print("波动率为:",a.std())