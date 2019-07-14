import pymysql


def conn_mysql():
    conn = pymysql.connect(user='root', db='read_book', password='123456',
                           host='127.0.0.1', port=3306, charset='utf8')
    return conn

def input_read_book(name,pwd,emil,sex,type):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "insert into user (username,pwd,emil,sex,author) values ('%s','%s','%s','%s','%s')" % (name, pwd, emil,sex,type )
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def check_read_book(name):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "select pwd from user where username='%s'" % (name)
    cursor.execute(sql)
    pwd_get = cursor.fetchall()
    if pwd_get == ():
        return True
    else:
        return False

def get_pwd(name):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "select pwd from user where username='%s'" % (name)
    cursor.execute(sql)
    pwd_get = cursor.fetchall()
    conn.close()
    a = pwd_get[0][0]
    return a

def allmassage_user(name):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from user where username='%s'" % (name)
    cursor.execute(sql)
    allmassage_user= cursor.fetchall()
    conn.close()
    return allmassage_user


def allmassage_user_all_all():
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from user "
    cursor.execute(sql)
    allmassage_user= cursor.fetchall()
    conn.close()
    return allmassage_user

def select_works(name):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select works from user where username='%s' "%(name)
    cursor.execute(sql)
    allmassage_user = cursor.fetchall()
    conn.close()
    if allmassage_user[0]['works']==None or allmassage_user[0]['works']=='' :
        return ' '
    else:
        return allmassage_user[0]['works']


def updata_works(works,username):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "update user set works='%s'  where username='%s' " % (works,username)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def update_clicks_all(bookname):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "update book set clicks=clicks+1  where book_name='%s' " % (bookname)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def delect_user(username):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "DELETE  FROM user WHERE username='%s' "%(username)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
