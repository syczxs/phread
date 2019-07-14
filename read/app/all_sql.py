import pymysql


def conn_mysql():
    conn = pymysql.connect(user='root', db='read_book', password='123456',
                           host='127.0.0.1', port=3306, charset='utf8')
    return conn

def get_user_information_user(name):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from user,user_information where user.username=user_information.username and user.username='%s'" % (name)
    cursor.execute(sql)
    allmassage_user_information= cursor.fetchall()
    conn.close()
    return allmassage_user_information

def select_by_book(name):
    name='%'+name+'%'
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from book where book_name like '%s'" % (name)
    cursor.execute(sql)
    allmassage_user_information= cursor.fetchall()
    conn.close()
    return allmassage_user_information

def select_by_author(name):
    name='%'+name+'%'
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from book where author like '%s'" % (name)
    cursor.execute(sql)
    allmassage_user_information= cursor.fetchall()
    conn.close()
    return allmassage_user_information

