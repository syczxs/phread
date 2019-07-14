import pymysql


def conn_mysql():
    conn = pymysql.connect(user='root', db='read_book', password='123456',
                           host='127.0.0.1', port=3306, charset='utf8')
    return conn

def create_table_title_book(bookname):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "create table %s " \
          "(ID varchar(50) not null," \
          "title_number int(20)," \
          "title_name varchar(50)," \
          "title_content longtext," \
          "author_name varchar(20)," \
          "clicks int(20)," \
          "up_time varchar(50))"%(bookname)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def input_book_title(book_name,ID,title_number,title_name,title_content,author_name,clicks,up_time):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "insert into %s (ID,title_number,title_name,title_content,author_name,clicks,up_time) values ('%s','%s','%s','%s','%s','%s','%s')" % (book_name,ID,title_number,title_name,title_content,author_name,clicks,up_time )
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def get_book_title(bookname):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from %s " % (bookname)
    cursor.execute(sql)
    all_massage = cursor.fetchall()
    conn.close()
    return all_massage

def ID_bookname(ID):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select book_name from book where ID='%s'" % (ID)
    cursor.execute(sql)
    all_massage = cursor.fetchall()
    conn.close()
    return all_massage

def get_book_title_number(bookname,title_number):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from %s where title_number=%s " % (bookname,title_number)
    cursor.execute(sql)
    all_massage = cursor.fetchall()
    conn.close()
    return all_massage

def get_book_title_number2(bookname,title_number):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from %s where title_number=%s " % (bookname,title_number)
    cursor.execute(sql)
    all_massage = cursor.fetchall()
    conn.close()
    massage = all_massage[0]['title_content'][0:200]
    return massage



def select_new(bookname):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select title_number from %s order by title_number desc " % (bookname)
    cursor.execute(sql)
    all_massage = cursor.fetchall()
    conn.close()
    massage = all_massage[0]
    return massage['title_number']

def updata_clicks(bookname,title_number):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "update `%s` set clicks=clicks+1 where title_number='%s' " % (bookname,title_number)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def sum_clicks(bookname):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select sum(clicks) from `%s` " %(bookname)
    cursor.execute(sql)
    all_massage = cursor.fetchall()
    print(all_massage)
    if all_massage[0]['sum(clicks)']==None:
        return 0
    else:
        return int(all_massage[0]['sum(clicks)'])

