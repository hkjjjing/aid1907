Tom lei le le 累了 累了

import pymysql

class User:
    # 在初始化就 连接数据库
    def __init__(self, database):
        self.db = pymysql.connect(user='root',
                                  password='123456',
                                  database = database,
                                  charset='utf8')
        self.cur = self.db.cursor()

    # 登录
    def login(self, name, passwd):
        sql = "select * from user where name = %s and passwd = %s"
        self.cur.execute(sql, [name, passwd])
        r = self.cur.fetchone()
        if r:
            return True

    # 注册
    def register(self, name, passwd):
        sql = "select * from user where name = %s"
        self.cur.execute(sql, [name])
        r = self.cur.fetchone()
        # 查找到说明用户存在
        if r:
            return False
        # 插入用户密码
        sql = "insert into user (name,password) values (%s, %s)"
        try:
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()

if __name__ == '__main__':
    user = User('stu')
    if user.register('Abby', '132'):
        print('注册成功')
    # if user.login('Abby', '132'):
    #     print('登录成功')
