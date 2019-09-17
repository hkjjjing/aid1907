'''
write_db.py
pymysql 写演示操作（insert ）
'''

import pymysql

# 链接数据库
db = pymysql.connect(user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

# 获取游标
cur = db.cursor()

# 执行sql语句
# name = input('Name:')
# age = input('Age:')
# score = input('Score:')
try:
    # # 合成一个正确的sql语句才能正确commit
    # sql = "insert into class values(10,'{0}','{1}','w','{2}');".format(name, age, score)
    # cur.execute(sql)  # 执行语句
    # db.commit()   # 同步数据库

    # # sql语句参量可以通过execute传入
    # sql = "insert into class values(11,'%s',%s,'w',%s);"
    # cur.execute(sql, [name, age, score])

    # 修改语句
    sql = "update class set score = 91 where name = 'Abby';"
    cur.execute(sql)
    sql = "delete from class where name = 'xm';"
    cur.execute(sql)

    db.commit()
except Exception as e:
    print(e)
    db.rollback()  # 回滚到没有commit这些语句前的状态

cur.close()
db.close()