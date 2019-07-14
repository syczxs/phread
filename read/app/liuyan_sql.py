import pymysql


def conn_mysql():
    conn = pymysql.connect(user='root', db='read_book', password='123456',
                           host='127.0.0.1', port=3306, charset='utf8')
    return conn


def get_liyan(bookname,title_number):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from liuyan where bookname='%s'and title_name='%s' " % (bookname,title_number)
    cursor.execute(sql)
    all_massage = cursor.fetchall()
    conn.close()
    return all_massage

def input_liuyan(username,liuyan,up_time,bookname,title_number):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "insert into liuyan(username,liuyan,up_time,bookname,title_name) values ('%s','%s','%s','%s','%s')" % (username,liuyan,up_time,bookname,title_number)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


