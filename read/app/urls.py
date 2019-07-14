from django.urls import path

from app.views import login, register, index, Exit, personal, all_information, up_file1, up_file2, create_book, contant, \
    write_book, read_story, push_money, buy_title, next_title, back_title, booktype, xinxi, yidu, roots, liuyan, sousuo, \
    collection, delect_shoucang, clicks_rank, delect_user_from

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('index/', index, name='index'),
    path('all_information/', all_information, name='all_information'),
    path('Exit/', Exit, name='Exit'),
    path('personal/', personal, name='personal'),
    path('create_book/', create_book, name='create_book'),
    path('up_file1/', up_file1, name='up_file1'),
    path('up_file2/', up_file2, name='up_file2'),
    path('contant/<str:bookname>/', contant, name='contant'),
    path('write_book/<str:ID>/<str:bookname>/<str:author>/', write_book, name='write_book'),
    path('read_story/<str:ID>/<int:title_number>/', read_story, name='read_story'),
    path('push_money/', push_money, name='push_money'),
    path('buy_title/<str:ID>/<int:title_number>/', buy_title, name='buy_title'),
    path('next_title/<str:ID>/<int:title_number>/', next_title, name='next_title'),
    path('back_title/<str:ID>/<int:title_number>/', back_title, name='back_title'),
    path('booktype/<str:booktype>/', booktype, name='booktype'),
    path('xinxi/', xinxi, name='xinxi'),
    path('yidu/<str:sendtime>', yidu, name='yidu'),
    path('roots/', roots, name='roots'),
    path('liuyan/<str:ID>/<int:title_number>/', liuyan, name='liuyan'),
    path('sousuo/', sousuo, name='sousuo'),
    path('collection/<str:bookname>/', collection, name='collection'),
    path('delect_shoucang/<str:bookname>/', delect_shoucang, name='delect_shoucang'),
    path('clicks_rank/', clicks_rank, name='clicks_rank'),
    path('delect_user_from/<str:username>/', delect_user_from, name='delect_user_from'),
]
