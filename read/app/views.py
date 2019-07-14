import datetime
import json
import os
import time

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.all_sql import get_user_information_user, select_by_book, select_by_author
from app.book_sql import input_creat_read_book, user_book_massage, all_book_massage, name_book_massage, updata_chapter, \
    clicks_rank_a
from app.history_sql import input_user_history, get_user_hitory_True, user_read_all_history
from app.information_sql import input_send_information, get_send_information, yidu_information
from app.liuyan_sql import input_liuyan, get_liyan
from app.other import authq
from app.title_sql import create_table_title_book, input_book_title, get_book_title, ID_bookname, get_book_title_number, \
    get_book_title_number2, select_new, updata_clicks, sum_clicks
from app.user_information import get_user_information, input_user_information, update_user_information
from app.user_vipsql import input_user_vip, get_allmassage_vip, updata_user_vip, updata_user_money, buy_titlesql
from app.usersql import check_read_book, input_read_book, get_pwd, allmassage_user, allmassage_user_all_all, \
    select_works, updata_works, update_clicks_all, delect_user


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        name = request.POST.get('name')
        pwd = request.POST.get('password')
        print(name)
        try:
            if get_pwd(name) == pwd:

                response = redirect(index)
                vip = get_allmassage_vip(name)[0]['vip']
                money = get_allmassage_vip(name)[0]['money']
                dict_cookie = {'name': name, 'pwd': pwd, 'vip': vip, 'money': money}
                response.set_cookie('aaa', json.dumps(dict_cookie), max_age=60 * 60)
                print(response)
                return response
            else:
                print("ddd")
                return render(request, 'login.html', {'date': '用户名不存在或密码错误'})
        except:
            return render(request, 'login.html', {'date': '登陆失败，请输入正确的用户名，密码'})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        name = request.POST.get('name')
        pwd = request.POST.get('password')
        pwd2 = request.POST.get('password2')
        emil = request.POST.get('emial')
        sex = request.POST.get('sex')
        type = request.POST.get('type')
        if sex == 'man':
            lujing = '/static/head/man.jpg'
        else:
            lujing = '/static/head/woman.jpg'
        input_user_information(name, lujing)
        vip = 0
        money = 0
        try:
            if pwd == pwd2:
                if check_read_book(name) == True:
                    input_user_vip(name, vip, money)
                    input_read_book(name, pwd, emil, sex, type)
                    return render(request, 'login.html', {'date1': '注册成功'})
                if check_read_book(name) == False:
                    return render(request, 'register.html', {'date': '用户名已被注册'})
            else:
                return render(request, 'register.html', {'date': '两次输入密码不同'})
        except:
            return render(request, 'register.html', {'date': '注册失败，请输入正确的用户名，密码'})


def auth(request):
    data_cookie = request.COOKIES.get('aaa')
    if not data_cookie:
        data_cookies = {'name': 0, 'pwd': 0, 'vip': 0, 'money': 0}
        return data_cookies
    else:
        data_cookie = request.COOKIES.get('aaa')
        data_cookies = json.loads(data_cookie)
        print(data_cookies)
        return data_cookies

def authq(func):
    def inner(request):
        data_cookie = request.COOKIES.get('aaa')
        if not data_cookie:
            data_cookies = {'name': 0, 'pwd': 0, 'vip': 0, 'money': 0}
            return func(data_cookies)
        else:
            data_cookie = request.COOKIES.get('aaa')
            data_cookies = json.loads(data_cookie)
            print(data_cookies)
            return func(data_cookies)
    return inner

def index(request):
    data_cookies = auth(request)
    name = data_cookies['name']
    if name == 0:
        date_allmassage = None
        date_vip = None
        date_touxiang = None
    else:
        date_allmassage = allmassage_user(name)[0]
        date_vip = get_allmassage_vip(name)[0]
        date_touxiang = get_user_information(name)[0]['pic']
    allbook_massage = all_book_massage

    return render(request, 'index.html', {'name': name, 'date_vip': date_vip, 'date_touxiang': date_touxiang,
                                          'date_allmassage': date_allmassage, 'allbook_massage': allbook_massage,
                                          'data_cookies': data_cookies})


def Exit(request):
    response = render(request, 'zhuxiao.html')
    response.delete_cookie('aaa')
    return response


def personal(request):
    data_cookies = auth(request)
    name = data_cookies['name']
    send_information = get_send_information(name)
    if not name:
        all_user_manage = None
        hobby = None
        book_masssge = None
    else:
        all_user_manage = get_user_information_user(name)[0]
        book_masssge = user_book_massage(name)
        a = all_user_manage['hobby'].split(",")
        hobby = a[1:len(a)]
        user_read_history = user_read_all_history(name)
    love = select_works(name).split(",")
    return render(request, 'personal.html',

                  {'all_user_manage': all_user_manage, 'hobby': hobby, 'book_massage': book_masssge,
                   'user_read_history': user_read_history, 'send_information': send_information, 'love': love})


def all_information(request):
    data_cookies = auth(request)
    name = data_cookies['name']
    if request.method == 'GET':
        return render(request, 'all_information.html')
    else:
        up_file = request.FILES.get('head_pic')
        age = request.POST.get('age', None)
        sex = request.POST.get('sex', None)
        hobby = request.POST.getlist('hobby')
        hobbys = ''
        for i in range(len(hobby)):
            hobbys = hobbys + ',' + str(i)
        if age and sex and hobby:
            if up_file:
                head_name = up_file.name
                file_path = os.path.join('static/head', head_name)
                f = open(file_path, 'wb+')
                for chunk in up_file.chunks():
                    f.write(chunk)
                f.close()
                lujing_head = '/static/head/' + head_name
                update_user_information(age, sex, hobbys, lujing_head, name)
                return HttpResponse('更新成功')
            else:
                if sex == 'man':
                    lujing_head = '/static/head/man.jpg'
                else:
                    lujing_head = '/static/head/woman.jpg'
            update_user_information(age, sex, hobbys, lujing_head, name)
            return HttpResponse('更新成功')
        else:
            return HttpResponse('更新失败')


def create_book(request):
    data_cookies = auth(request)
    name = data_cookies['name']
    if request.method == 'GET':
        return render(request, 'create_book.html')
    else:
        up_file = request.FILES.get('pic')
        book_name = request.POST.get('name')
        book_type = request.POST.get('type')
        jianjie = request.POST.get('jieshao')
        ID = str(time.time()) + name
        now = datetime.datetime.now()
        if book_name and book_type and jianjie and ID and now:
            if up_file:
                book_pic_name = up_file.name
                file_path = os.path.join('static/book_pic', book_pic_name)
                f = open(file_path, 'wb+')
                for chunk in up_file.chunks():
                    f.write(chunk)
                f.close()
                book_pic = '/static/book_pic/' + book_pic_name
                input_creat_read_book(ID, book_name, name, 0, book_type, now, jianjie, book_pic, 1, 0, 0)
                create_table_title_book(book_name)
                return HttpResponse('创建成功1')
            else:
                book_pic = '/static/book_pic/wei.jpg'
                input_creat_read_book(ID, book_name, name, 0, book_type, now, jianjie, book_pic)
                create_table_title_book(book_name)
                return HttpResponse('创建成功2')
        else:
            return HttpResponse('创建失败')


def up_file1(request):
    pass


def up_file2(request):
    pass


def contant(request, bookname):
    data_cookies = auth(request)
    name = data_cookies['name']
    if name == 0:
        date_allmassage = None
        date_vip = None
        date_touxiang = None
    else:
        date_allmassage = allmassage_user(name)[0]
        date_vip = get_allmassage_vip(name)[0]
        date_touxiang = get_user_information(name)[0]['pic']
    allbook_massage = name_book_massage(bookname)[0]
    book_title = get_book_title(bookname)
    sum = sum_clicks(bookname)
    return render(request, 'contant.html',
                  {'name': name, 'allbook_massage': allbook_massage, 'book_title': book_title,
                   'data_cookies': data_cookies
                      , ' date_allmassage': date_allmassage, 'date_vip': date_vip, 'date_touxiang': date_touxiang,
                   'sum': sum})


def write_book(request, ID, bookname, author):
    if request.method == 'GET':
        return render(request, 'write_book.html', {'ID': ID, 'bookname': bookname, 'author': author})
    else:
        title_number = request.POST.get('title_number')
        title_name = request.POST.get('title_name')
        title_content = request.POST.get('title_contant')
        now = datetime.datetime.now()
        clicks = 0
        input_book_title(bookname, ID, title_number, title_name, title_content, author, clicks, now)
        updata_chapter(title_number, ID)

    return HttpResponse('上传成功')


def read_story(request, ID, title_number):
    data_cookies = auth(request)
    name = data_cookies['name']
    if name == 0:
        date_allmassage = None
        date_vip = None
        date_touxiang = None
    else:
        date_allmassage = allmassage_user(name)[0]
        date_vip = get_allmassage_vip(name)[0]
        date_touxiang = get_user_information(name)[0]['pic']
    bookname = ID_bookname(ID)[0]['book_name']
    massage = get_book_title_number(bookname, title_number)[0]
    massage2 = get_book_title_number2(bookname, title_number)
    now = datetime.datetime.now()
    now2 = int(time.time())
    news = select_new(bookname)
    updata_clicks(bookname, title_number)
    update_clicks_all(bookname)
    liuyanneirong = get_liyan(bookname, title_number)
    if name != 0 and massage['title_number'] < 4:
        if get_user_hitory_True(name, massage['title_number'], bookname) == True:
            input_user_history(name, bookname, massage['title_name'], massage['title_number'], now, now2)

            a = 0
        else:
            a = 0
    if name != 0 and massage['title_number'] >= 4:
        if get_user_hitory_True(name, massage['title_number'], bookname) == True:
            a = 1
        if get_user_hitory_True(name, massage['title_number'], bookname) == False:
            a = 0
    else:
        a = 0

    return render(request, 'read.html', {'massage': massage, 'date_touxiang': date_touxiang,
                                         'date_allmassage': date_allmassage,
                                         'data_cookies': data_cookies, 'date_vip': date_vip,
                                         'massage2': massage2, 'a': a, 'news': news, 'liuyanneirong': liuyanneirong})


def push_money(request):
    data_cookies = auth(request)
    username = data_cookies['name']
    if request.method == 'GET':
        return render(request, 'push.html')
    else:
        money = request.POST.get('money')
        if money:
            updata_user_money(username, money)
        vip = request.POST.get('vip')
        if vip:
            updata_user_vip(username, int(vip))
        data = '恭喜你充值成功'
        return render(request, 'push.html', {'data': data})


def buy_title(request, ID, title_number):
    data_cookies = auth(request)
    name = data_cookies['name']
    vip_title = request.POST.get('vip_title')
    bookname = ID_bookname(ID)[0]['book_name']
    massage = get_book_title_number(bookname, title_number)[0]
    now = datetime.datetime.now()
    now2 = int(time.time())
    if vip_title == '1':
        date_vip = get_allmassage_vip(name)[0]
        if date_vip['money'] < 1:
            return HttpResponse('余额不足请充值')
        else:
            buy_titlesql(name)
        input_user_history(name, bookname, massage['title_name'], title_number, now, now2)
        return HttpResponse('购买成功')


def next_title(request, ID, title_number):
    title_number = title_number + 1
    data_cookies = auth(request)
    name = data_cookies['name']
    if name == 0:
        date_allmassage = None
        date_vip = None
        date_touxiang = None
    else:
        date_allmassage = allmassage_user(name)[0]
        date_vip = get_allmassage_vip(name)[0]
        date_touxiang = get_user_information(name)[0]['pic']
    bookname = ID_bookname(ID)[0]['book_name']
    massage = get_book_title_number(bookname, title_number)[0]
    massage2 = get_book_title_number2(bookname, title_number)
    now = datetime.datetime.now()
    now2 = int(time.time())
    news = select_new(bookname)
    updata_clicks(bookname, title_number)
    update_clicks_all(bookname)
    if name != 0 and massage['title_number'] < 4:
        if get_user_hitory_True(name, massage['title_number'], bookname) == True:
            input_user_history(name, bookname, massage['title_name'], massage['title_number'], now, now2)

            a = 0
        else:
            a = 0
    if name != 0 and massage['title_number'] >= 4:
        if get_user_hitory_True(name, massage['title_number'], bookname) == True:
            a = 1
        if get_user_hitory_True(name, massage['title_number'], bookname) == False:
            a = 0

    return render(request, 'read.html', {'massage': massage, 'date_touxiang': date_touxiang,
                                         'date_allmassage': date_allmassage,
                                         'data_cookies': data_cookies, 'date_vip': date_vip,
                                         'massage2': massage2, 'a': a, 'news': news})


def back_title(request, ID, title_number):
    title_number = title_number - 1
    data_cookies = auth(request)
    name = data_cookies['name']
    if name == 0:
        date_allmassage = None
        date_vip = None
        date_touxiang = None
    else:
        date_allmassage = allmassage_user(name)[0]
        date_vip = get_allmassage_vip(name)[0]
        date_touxiang = get_user_information(name)[0]['pic']
    bookname = ID_bookname(ID)[0]['book_name']
    massage = get_book_title_number(bookname, title_number)[0]
    massage2 = get_book_title_number2(bookname, title_number)
    now = datetime.datetime.now()
    now2 = int(time.time())
    news = select_new(bookname)
    updata_clicks(bookname, title_number)
    update_clicks_all(bookname)
    if name != 0 and massage['title_number'] < 4:
        if get_user_hitory_True(name, massage['title_number'], bookname) == True:
            input_user_history(name, bookname, massage['title_name'], massage['title_number'], now, now2)

            a = 0
        else:
            a = 0
    if name != 0 and massage['title_number'] >= 4:
        if get_user_hitory_True(name, massage['title_number'], bookname) == True:
            a = 1
        if get_user_hitory_True(name, massage['title_number'], bookname) == False:
            a = 0

    return render(request, 'read.html', {'massage': massage, 'date_touxiang': date_touxiang,
                                         'date_allmassage': date_allmassage,
                                         'data_cookies': data_cookies, 'date_vip': date_vip,
                                         'massage2': massage2, 'a': a, 'news': news})


def booktype(request, booktype):
    data_cookies = auth(request)
    name = data_cookies['name']
    if name == 0:
        date_allmassage = None
        date_vip = None
        date_touxiang = None
    else:
        date_allmassage = allmassage_user(name)[0]
        date_vip = get_allmassage_vip(name)[0]
        date_touxiang = get_user_information(name)[0]['pic']
    allbook_massage = all_book_massage
    return render(request, 'book_type.html', {'name': name, 'date_vip': date_vip, 'date_touxiang': date_touxiang,
                                              'date_allmassage': date_allmassage, 'allbook_massage': allbook_massage,
                                              'data_cookies': data_cookies, 'booktype': booktype})


def xinxi(request):
    sendname = request.POST.get('name')
    contant = request.POST.get('contant')
    data_cookies = auth(request)
    name = data_cookies['name']
    now = datetime.datetime.now()
    input_send_information(name, sendname, contant, now, '浏览')
    return HttpResponse('发送成功')


def yidu(request, sendtime):
    yidu_information(sendtime)
    return HttpResponse('更新成功')


def roots(request):
    allmassage_user_all = allmassage_user_all_all()
    print(allmassage_user_all)
    return render(request, 'roots.html', {'allmassage_user_all': allmassage_user_all})


def liuyan(request, ID, title_number):
    bookname = ID_bookname(ID)[0]['book_name']
    data_cookies = auth(request)
    name = data_cookies['name']
    contant = request.POST.get('contant')
    now = datetime.datetime.now()
    input_liuyan(name, contant, now, bookname, title_number)
    return HttpResponse('留言成功')


def sousuo(request):
    select = request.POST.get('select')
    massage1 = select_by_book(select)
    massage2 = select_by_author(select)
    if massage1 == ():
        return render(request, 'sousuo.html', {'massage': massage2})
    if massage2 == ():
        return render(request, 'sousuo.html', {'massage': massage1})


def collection(request, bookname):
    data_cookies = auth(request)
    name = data_cookies['name']
    works = select_works(name)
    if works == ' ':
        works = bookname
    else:
        works = works + ',' + bookname
    updata_works(works, name)
    return HttpResponse('收藏成功')


def delect_shoucang(request, bookname):
    print(bookname, 'aaa')
    data_cookies = auth(request)
    name = data_cookies['name']
    a = select_works(name).split(",")
    print(a)
    a.remove(bookname)
    b = ' '
    for i in a:
        if b == ' ':
            b = i
        else:
            b = b + ',' + i
    updata_works(b, name)
    return HttpResponse('取消成功')


def clicks_rank(request):
    data_cookies = auth(request)
    name = data_cookies['name']

    if name == 0:
        date_allmassage = None
        date_vip = None
        date_touxiang = None
    else:
        date_allmassage = allmassage_user(name)[0]
        date_vip = get_allmassage_vip(name)[0]
        date_touxiang = get_user_information(name)[0]['pic']
    massage = clicks_rank_a
    return render(request, 'clicks.html',
                  {'masssage': massage, ' date_allmassage': date_allmassage, 'date_vip': date_vip,
                   'date_touxiang': date_touxiang, 'data_cookies': data_cookies})


def delect_user_from(request, username):
    delect_user(username)
    return HttpResponse('删除成功')
