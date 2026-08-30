import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams["font.family"] = "SimHei"
print(plt.figure(figsize = (10,5)))
#要绘图的数据
subject = ["语文","数学","英语","科学"]
scores = [85,92,78,88]

#绘制柱状图
plt.bar(subject,scores,
        label="小红",
        color = "orange",
        width = 0.6)
#添加标题
plt.title("2025成绩分布",color = "red",fontsize = 20)
#加上坐标轴标签
plt.xlabel("科目",fontsize = 10)
plt.ylabel("销售额",fontsize = 10)
#添加图例
plt.legend(loc = "upper left",fontsize = 10)
#添加网格线
plt.grid(axis="y",alpha = 0.5,color = "grey",linestyle = "--")
#设置y轴的范围
plt.ylim(0,100)
#在每个数据点上显示数值
for x,y in zip(subject,scores):
    plt.text(x,y+1,str(y),ha= "center",va= "top",fontsize = 10)
#自动优化排版
plt.tight_layout()
print(plt.show())

