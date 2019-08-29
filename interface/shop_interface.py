from db import db_handler
from core import src
from interface import bank_interface
#商城结算接口
def shop_pay_interface(username,shopping_car,cost):
    #1、调用银行支付接口
    flag=bank_interface.pay_interface(username,cost)
    #获取当前用户
    user_dic=db_handler.select(username)
    #判断是否支付成功！
    #如果支付成功，清空购物车
    if flag:
        user_dic['shopping_car']={}
        db_handler.save(user_dic)
        return True,f'购物并支付成功'
    #若支付失败，保存购物车
    else:
        user_dic['shopping_car']=shopping_car
        db_handler.save(user_dic)
        return False,f'支付失败，保存购物车'


#将商品添加到购物车接口
def shopping_car_interface(username,shopping_car):
    #1、获取当前用户
    user_dic=db_handler.select(username)

    #2、商品添加到购物车
    if shopping_car:
        #如果有商品就把商品添加到购物车字典中
        user_dic['shopping_car']=shopping_car
        db_handler.save(user_dic)
        return True,f'商品添加到购物车成功'
    else:
        return False,f'购物车为空！'

#查看购物车接口

def watch_shop_interface(username):
    user_dic=db_handler.select(username)
    #将用户字典中的购物车商品返回出来
    return user_dic.get('shopping_car')












