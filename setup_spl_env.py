import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Create / connect to database
conn = sqlite3.connect("demo.db")
cursor = conn.cursor()

# 2. Create table and insert sample data
cursor.execute("DROP TABLE IF EXISTS sales")
cursor.execute("""
    CREATE TABLE sales (
        region TEXT,
        product TEXT,
        amount REAL,
        date TEXT
    )
""")

data = [
    ("East", "A", 1200, "2026-01-15"),
    ("South", "B", 800, "2026-02-20"),
    ("East", "A", 1500, "2026-03-10"),
    ("North", "C", 600, "2026-04-05"),
    ("South", "B", 900, "2026-05-18"),
    ("East", "C", 1100, "2026-06-22"),
]

cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?)", data)
conn.commit()

# 3. SQL query + pandas read
df = pd.read_sql_query(
    "SELECT region, SUM(amount) AS total_sales FROM sales GROUP BY region",
    conn
)

print("Query result:")
print(df)

# 4. Plot
df.plot(x="region", y="total_sales", kind="bar", legend=False)
plt.title("Total Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# 5. Close connection
conn.close()

print("Done. demo.db has been created.")

#数据库，持久手段，数据库储存
#数据库的概念：数据库是长期存在于计算机内，有组织的，可供享的大量数据的集合文件
#特点：就是磁盘中以特定的格式存储
#存储在数据库中，不主动删除就不会消失
#方便对数据读写删改


#数据库类型：关系型与非关系型
#非关系型：没有统一建设标准，性能较高（键值key,value，文档，JSON等，内部的数据结构多）
#关系型：按照类别进行存储，表与表进行关联操作，性能相对一般（）
#结构化数据库：结构较为固定，不同东西分别存储到不同的库，ACID可以保证转账失败，而钱不损失
#丰富查询语句：查询学生及学生的分数

#数据库的类型选择：一般主体数据存储在关系型数据库，缓存数据与高并发在非关系形数据库

#关系型数据库的存储设计规则：E-R模型，关系型数据库一类数据对应一张表储存，表和表可以通过“关系”进行多表操作
#四单位：库，表，列，行

#数据库相当于一个仓库
#数据库管理系统DBMS，是间接管理数据库的数据
#oracle（行业标杆，企业收费极为昂贵）,其次MYSQL（前两者都为关系型，性能优异，中小项目，企业开源免费），再是DB2（金融项目，企业收费极为昂贵），最后是SQLite（嵌入式数据库），比较小型，适合移动设备，企业开源免费
#我们学习用