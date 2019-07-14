import pymysql


def conn_mysql():
    conn = pymysql.connect(user='root', db='read_book', password='123456',
                           host='127.0.0.1', port=3306, charset='utf8')
    return conn

def input_user_history(name,bookname,title_name,title_id,readtime,time2):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "insert into user_readhistory (username,bookname,title_name,title_id,read_time,orders) values ('%s','%s','%s',%s,'%s',%s)" % (name,bookname,title_name,title_id,readtime,time2)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def get_user_hitory_True(username,title_number,book_name):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "select * from user_readhistory where username='%s' and title_id=%s and bookname='%s'"  % (username,title_number,book_name)
    cursor.execute(sql)
    all_massage = cursor.fetchall()
    conn.close()
    if all_massage==():
        return True
    else:
        return False

def user_read_all_history(name):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from user_readhistory where username='%s' order by orders desc " % (name)
    cursor.execute(sql)
    all_massage= cursor.fetchall()
    conn.close()
    return all_massage[0:5]

