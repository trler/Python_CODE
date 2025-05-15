# 反向写入 从mysql中的数据 利用python代码 读取出来 利用select语句 写成json文件 导出
from pymysql import Connection
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="lcx1234321",
    autocommit=True,
)
cursor = conn.cursor()
conn.select_db("py_sql")
f = open('作业.txt','w',encoding='utf-8')
sql =(f'select * from orders')
cursor.execute(sql)
result:tuple = cursor.fetchall()
print(result)
for row in result:
    f.write(f'{{"data":"{row[0]}"，"order_id":"{row[1]},"money":{row[2]},"province":"{row[3]}"}}\n')
f.close()
conn.close()