import pymysql


def conn_mysql():
    conn = pymysql.connect(user='root', db='read_book', password='123456',
                           host='127.0.0.1', port=3306, charset='utf8')
    return conn


def get_send_information(sendname):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from information where sendname='%s' " % (sendname)
    cursor.execute(sql)
    all_massage = cursor.fetchall()
    conn.close()
    return all_massage

def input_send_information(username,sendname,xinxi,sendtime,states):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "insert into information (username,sendname,xinxi,sendtime,states) values ('%s','%s','%s','%s','%s')" % (username,sendname,xinxi,sendtime,states)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def yidu_information(sendtime):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "update information set states='已浏览'  where sendtime='%s' " % (sendtime)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

