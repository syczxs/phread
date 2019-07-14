import pymysql


def conn_mysql():
    conn = pymysql.connect(user='root', db='read_book', password='123456',
                           host='127.0.0.1', port=3306, charset='utf8')
    return conn

def input_creat_read_book(ID,book_name,name,chapter,book_type,now,jianjie,book_pic,free,overs,clicks):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "insert into book (ID,book_name,author,chapter,book_type,start_time,last_time,jianjie,book_pic,free,overs,clicks) values " \
          "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (ID,book_name,name,chapter,book_type,now,now,jianjie,book_pic,free,overs,clicks)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
def all_book_massage():
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from book "
    cursor.execute(sql)
    all_massage= cursor.fetchall()
    conn.close()
    return all_massage

def user_book_massage(name):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from book where author='%s'" % (name)
    cursor.execute(sql)
    all_massage= cursor.fetchall()
    conn.close()
    return all_massage

def type_book_massage(book_type):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from book where author='%s'" % (book_type)
    cursor.execute(sql)
    all_massage= cursor.fetchall()
    conn.close()
    return all_massage

def name_book_massage(name):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from book where book_name='%s'" % (name)
    cursor.execute(sql)
    all_massage= cursor.fetchall()
    conn.close()
    return all_massage

def updata_chapter(title_number,ID):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "update book set chapter=%s where ID='%s' " % (title_number,ID)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()



def clicks_rank_a():
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from book order by clicks desc"
    cursor.execute(sql)
    all_massage = cursor.fetchall()
    conn.close()
    return all_massage


