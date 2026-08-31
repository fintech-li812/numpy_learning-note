#绘制条形图
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams["font.family"] = "SimHei"
print(plt.figure(figsize = (10,5)))
#添加标题
plt.title("2025GDP排名",color = "red",fontsize = 20)
countries = ["China","United States","Japan","Germany","Italy"]
GDP =[92,88,43,32,29]
#绘制条形图
plt.barh(countries,GDP)
plt.tight_layout()
plt.show()
#有不同类别的比较使用条形图








