

from db import db_handler
#查看余额接口
def chakan_money_interface(username):

    user_dic=db_handler.select(username)
    return user_dic.get('money')


#提现接口
def tixian_interface(username,money):
    user_dic=db_handler.select(username)
    tixian_money=money*1.05
    if user_dic['money'] >= tixian_money:
        user_dic['money']-=tixian_money

        msg=f'{username}提现{money}元成功！'
        #记录流水
        user_dic['money_water'].append(msg)

        db_handler.save(user_dic)
        return True,msg
    else:
        return False,f'{username}你个穷鬼，请充值RMB'




#还款接口
def huankuan_interface(username,money):
    user_dic=db_handler.select(username)
    user_dic['money']+=money
    msg=f'{username}还款{money}元成功'
    #记录流水
    user_dic['money_water'].append(msg)

    db_handler.save(user_dic)
    return msg



#转账接口
def zhuanzhang_interface(username,to_user,money):
    #1、判断用户是否存在
    to_user_dic=db_handler.select(to_user)
    if  not to_user_dic:
        return False,f'目标用户 不存在！'
    #2、取出钱后判断用户的余额是否充足
    user_dic=db_handler.select(username)
    if user_dic.get('money') >= money :
    #3、当前用户金钱足够，向目标用户转账，目标用户加钱
        #自己减少钱
        user_dic['money'] -= money
        #对方增加钱
        to_user_dic['money'] += money
        msg=f'{username}向,{to_user},转账{money}元'
    #记录流水
        user_dic['money_water'].append(msg)
        msg1=f'{to_user}收到,{username},转账{money}元'
        user_dic['money_water'].append(msg1)

    #4、保存用户数据
        db_handler.save(user_dic)
        db_handler.save(to_user_dic)
        return True,msg
    return False,f'余额不足，转账失败'


#流水接口
def liushui_interface(username):
    user_dic=db_handler.select(username)
    return user_dic.get('money_water')


#银行支付接口
def pay_interface(username,cost):
    #查用户
    user_dic=db_handler.select(username)
    #查用户当前金额
    # user_dic.get('money')
    #判断用户当前金额是否可以支付购物车商品的总金额
    if user_dic.get('money') >= cost:
        #用户账户当前金额减去购物车商品总金额
        user_dic['money'] -=cost
        #记录流水
        msg=f'{username},购物支付{cost}元成功！！'
        user_dic['money_water'].append(msg)
        db_handler.save(user_dic)
        return True,msg

    return False
















