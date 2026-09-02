import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize= (10,5))
things = ["学习","娱乐","运动","睡觉","其他"]
times = [6,4,1,8,5]
colors = ["#66b3ff","#99ff99","#ffcc99","#ff9999","#ff4499"]#可以自己设置配色方案
#饼图的绘制
plt.pie(times,labels=things,
        autopct="%.1f%%",#百分比
        startangle=90,#调整初始角度
        colors=colors)
#饼图的配置
#添加标题
plt.title("一天的时间分布",color = "red",fontsize = 20)
#label直接显示在外圈
plt.tight_layout()
plt.show()
#绘制环形图
plt.figure(figsize= (10,5))
plt.pie(times,labels=things,
        autopct="%.1f%%",#百分比
        startangle=90,#调整初始角度
        colors=colors,
        wedgeprops={"width":0.6},#后面的数跟的是占比(宽度的百分比)，数字越小，圆环越细
        pctdistance=0.6)
plt.title("一天的时间分布",color = "red",fontsize = 20)
plt.text(0,0,"总计：\n100%",ha="center",va="center",fontsize = 20)
plt.tight_layout()
plt.show()
#绘制爆炸式饼图
plt.figure(figsize= (10,5))
things = ["学习","娱乐","运动","睡觉","其他"]
times = [6,4,1,8,5]
colors = ["#66b3ff","#99ff99","#ffcc99","#ff9999","#ff4499"]
explode = [0.1,0,0,0,0]#0.1是突出的部分，一般是0。1或者0.2
plt.pie(times,labels=things,
        autopct="%.1f%%",
        startangle=90,
        colors=colors,
        explode= explode,
        shadow=True)#突出那一块重点，加上阴影
#饼图的配置
#添加标题
plt.title("一天的时间分布",color = "red",fontsize = 20)
#label直接显示在外圈
plt.tight_layout()
plt.show()
