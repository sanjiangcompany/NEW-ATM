

from db import db_handler

#注册接口
def register_interface(username,password):
    user_dic=db_handler.select(username)
    if user_dic:
        return False,'用户名已存在！'
    else:
        #没有这个用户然后去注册该用户
        user_dic={
            'username':username,
            'password':password,
            'money':15000,
            'money_water':[],
            'lock':False,
            'shopping_car':{}

        }
        db_handler.save(user_dic)
        return True,f'{username}注册成功'

#登录接口
def login_interface(username,password):
    user_dic=db_handler.select(username)
    if not user_dic:
        return False,f'用户不存在'
    #检验密码
    if user_dic.get('password')==password:
        return True,f'{username}登录成功！'
    else:
        return False,f'密码错误！'


#注销接口
from core import src
def zhuxiao_interface(username):
    src.user_info['user']=None

    return '注销成功'


    # user_dic=db_handler.select(username)
    # user_dic.clear()
    # #这种是取出来在内存中，然后又清空该变量的内存，
    # # 与user_info其实压根没有什么关联
    # return '注销成功'
    #





