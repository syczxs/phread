import pymysql


def conn_mysql():
    conn = pymysql.connect(user='root', db='read_book', password='123456',
                           host='127.0.0.1', port=3306, charset='utf8')
    return conn

def input_user_vip(name,vip,money):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "insert into user_vip (username,vip,money) values ('%s','%s','%s')" % (name, vip,money )
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def get_allmassage_vip(name):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from user_vip where username='%s'" % (name)
    cursor.execute(sql)
    all_massage= cursor.fetchall()
    conn.close()
    return all_massage

def updata_user_money(name,money):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "update user_vip set money=money+%s  where username='%s' " % (money, name)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def updata_user_vip(name,vip):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "update user_vip set vip=%s where username='%s' " % (vip, name)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def buy_titlesql(name):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "update user_vip set money=money-1  where username='%s' " % (name)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

