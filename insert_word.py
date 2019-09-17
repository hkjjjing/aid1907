

import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

# 获取游标 （操作数据库，执行sql语句，获得执行结果）
cur = db.cursor()
sql = 'insert into words (word,mean) values (%s,%s);'
f = open('dict.txt')
for line in f:
    tmp = line.split(' ', 1)
    word = tmp[0]
    mean = tmp[1].strip()
    cur.execute(sql, [word, mean])   # 执行语句  但是没有提交
try:
    # 执行语句
    db.commit()  # 提交
except Exception as e:
    print(e)
    db.rollback()  # 回滚
cur.close()
db.close()
