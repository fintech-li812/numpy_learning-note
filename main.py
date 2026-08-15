#numpy基本实战训练
#成绩分析
import numpy as np
score = np.array([85,59,78,92,88])
print(score)
print(np.sort(score))
print("平均数：",np.mean(score))
print("标准差：""%.3f"%np.std(score))
print("中位数：""%.3f"%np.median(score))
#百分制与十分制
print(score/10)

#矩阵运算
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[3,2,1],[4,5,6],[7,8,9]])
#计算逐元素乘法
#A + B
print(A + B)
#A * B
print(A*B)
#矩阵乘法
print(A@B)
#print(np.dot(A,B))
#|1 2|  |5 6|
#|3 4|  |7 8|
#C11 = A[1:]*B[:1] = (1,2)*(5 7) 1*5 + 2*7 = 19
#C12 = A[1:]*B{:2} = (1,2)*(6,8) 1*6 + 2*8 = 22

#随机数据生成
#引入种子
np.random.seed(0)
arr = np.random.randint(0,30,(4,5))
#取大不取小，先范围后形状，整数数组
print(arr)
#每列的最大值加参数，axis为轴
#最大值
print(np.max(arr,axis=0))
#axis=0是列，=1是行
#最小值
print(np.min(arr,axis=0))
#替换数字
#布尔索引，最简单方法
#偶arr % 2 ==0,奇arr % 2 ==1

arr[arr%2==1]= -1
print(arr)
#arr = np.where(arr%2 ==1 , -1,arr)较为麻烦
#arr[][] = -1可以具体索引
#单独是行，[:,]是列
