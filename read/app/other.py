import json


def authq(func):
    def inner(request,*args):
        data_cookie = request.COOKIES.get('aaa')
        if not data_cookie:
            data_cookies = {'name': 0, 'pwd': 0, 'vip': 0, 'money': 0}
            return func(data_cookies=data_cookies)
        else:
            data_cookie = request.COOKIES.get('aaa')
            data_cookies = json.loads(data_cookie)
            print(data_cookies)
            return func

    return inner
