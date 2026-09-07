
#五种图表：
#折线图：plot
#条形图：bar
#饼图：pie
#散点图：scatter
#箱线图：boxplot
#多个图表
#组合图

#绘制折线图
import matplotlib.pyplot as plt
from matplotlib import rcParams #字体及其他属性
rcParams["font.family"] = "SimHei"#mac用STHeiti
#创建图表，设置大小
print(plt.figure(figsize = (10,5)))#实际上就是一块布
#要绘图的数据
month = ["1月","2月","3月","4月"]
sales = [100,150,80,130]
#绘制折线图(机器常用控制的参数)
plt.plot(month,sales,
         label= "产品A",
         color = "orange",
         linewidth = 2,
         linestyle= "--",
         marker="o")#先X轴，后Y轴,linewidth是线的宽度
#绘制之后进行配置
plt.title("2025年销售趋势",color = "pink",fontsize = 30)#标题是通用的
#添加坐标轴的标签
plt.xlabel("月份",fontsize = 10,color = "red")
plt.ylabel("销售额(万元)",fontsize = 10,color = "red")
#添加图例
plt.legend(loc = "upper left")
#添加网格线
plt.grid(axis="x",alpha = 0.5,color = "blue",linestyle="--")#True指的是两个方向的网格线都有,alpha是它的透明度,一般较浅
#设置刻度字体大小
plt.xticks(rotation=45,fontsize = 12)
plt.yticks(rotation=45,fontsize = 12)
#设置Y轴的范围(默认以最小的为最低值)
plt.ylim(0,160)
#在每个数据点上都显示数值（运用for）
for x,y in zip(month,sales):
    plt.text(x,y+1,str(y),ha="center",va="bottom",fontsize = 10)#str是要显示的数据，ha是水平居中的方式/left,right
#优点是灵活，但是复杂
#折线图看顶点数据
#显示图表
print(plt.show())
#一般要改的是中间的数据与配置