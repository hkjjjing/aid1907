'''
mysql.py
pymysql 操作数据库基本流程

'''

import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

# 获取游标 （操作数据库，执行sql语句，获得执行结果）
cur = db.cursor()

# 执行语句
sql = 'insert into class values(5, "Emma", 17, "w", 79);'
cur.execute(sql)   # 执行语句  但是没有提交

# 因为有写操作，所以要提交到数据库
db.commit()

# 关闭游标
cur.close()

# 关闭数据库
db.close()

