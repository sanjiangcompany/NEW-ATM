

#登录装饰器

from functools import wraps

def login_auth(func):
    from core import src
    @wraps(func)
    def inner(*args,**kwargs):

        if src.user_info.get('user'):
            res=func(*args,**kwargs)
            return res
        else:
            print('还没有登录，请去登录')
            src.login()


    return inner








