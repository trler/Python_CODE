# 基础使用
# 通过pymysql使用
from pandas.core.indexing import convert_from_missing_indexer_tuple
from pymysql import Connection
# 构建链接
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='lcx1234321',
)
print(conn.get_server_info())
# 执行非查询性质的sql
cursor = conn.cursor() # 游标对象
# 选择数据库
conn.select_db('test')
# 执行sql
# cursor.execute('create table test_pymysql2(id int);')

# 带有查询性质的sql
conn.select_db('world')
cursor.execute('select * from student1')

results:tuple = cursor.fetchall() # 嵌套元组
for r in results:
    print(r) # 20条结果
# print(results)










# 关闭链接
conn.close()

# 数据插入 执行sql语句到mysql
# commit 提交
# 直接执行语句时，默认需要通过代码“确认”commit 一下
#

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='lcx1234321',
    autocommit=True # 自动确认
)

cursor = conn.cursor()
conn.select_db('world')
# cursor.execute('create table student_py(id int, name varchar(20))')
for r in range(1,100):
    cursor.execute('insert into student_py values (10002,"林觉期间")')

# 确认机制  commmit
conn.commit()



# results:tuple = cursor.fetchall()

conn.close()