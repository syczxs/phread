import pymysql


def conn_mysql():
    conn = pymysql.connect(user='root', db='read_book', password='123456',
                           host='127.0.0.1', port=3306, charset='utf8')
    return conn

def input_user_information(name,lujing):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "insert into user_information (username,age,sex,hobby,pic) values ('%s','%s','%s','%s','%s')" % (name,None,None,None,lujing)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def get_user_information(name):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from user_information where username='%s'" % (name)
    cursor.execute(sql)
    allmassage_user_information= cursor.fetchall()
    conn.close()
    return allmassage_user_information

def update_user_information(age,sex,hobby,lujing_head,name):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "update  user_information set age='%s', sex='%s',hobby='%s',pic='%s' where username='%s' " %(age,sex,hobby,lujing_head,name)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


