import numpy as np
import pandas as pd
np.random.seed(42)
scores = pd.Series(np.random.randint(50,101,10),index=["学生"+str(i)for i in range(1,11)])
print(scores)
#indexes = []
#for i in range(1,11)
#   indexes.append("学生“+str(i))
#print(indexes)
#print(values)
print("平均分：",scores.mean())
print("最高分：",scores.max())
print("最低分：",scores.min())
#高于平均分的学生人数
mean = scores.mean()
print(scores[scores >= mean])
#三种求个数的操作
print("高于平均分的人数:",len(scores[scores >= mean]))#布尔索引
print("高于平均分的人数:",scores[scores >= mean].count())
print("高于平均分的人数:",scores[scores >= mean].size)
