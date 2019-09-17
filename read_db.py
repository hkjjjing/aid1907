'''
read_db.py
pymysql 读操作演示  (select)
'''

import pymysql

# 链接数据库
db = pymysql.connect(user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

# 获取游标
cur = db.cursor()

# 获取数据
sql = "select name,hobby from interest where hobby = 'sing,dance';"
cur.execute(sql)


# # 1. 可以直接遍历游标
# for i in cur:
#     print(i)

# # 2. 通过fetchall获取所有查询结果
# all_row = cur.fetchall()
# print(all_row)

# # 3. 获取查询的多个结果
# many_row = cur.fetchmany(1)
# print(many_row)


# 上面返回的都是元组套元组，下面这个返回一个结果，就一个元组
# 4. 获取一个查询结果
one_row = cur.fetchone()
print(one_row)



cur.close()
db.close()
