
from lib import common
from interface import bank_interface
from interface import user_interface
from interface import shop_interface
user_info = {

    'user':None

    }


#注册功能
def register():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请输入确认密码：').strip()
        if re_password == password:
            flag, msg = user_interface.register_interface(username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')

#登录功能
def login():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        flag, msg=user_interface.login_interface(username,password)
        if flag:
            print(msg)
            user_info['user'] = username
            break
        else:
            print(msg)

#查看余额功能

#登录装饰器
#查看余额功能
@common.login_auth
def check_money():
    print('欢迎来到查看余额功能！')
    money=bank_interface.chakan_money_interface(user_info['user'])
    print(money)


#提现功能
@common.login_auth
def tixian():
    while True:
        money=input('请输入要提现的金额：')
        if not  money.isdigit():
            print('必须是数字')
            continue
        else:
            money=int(money)
            flag,msg=bank_interface.tixian_interface(user_info['user'],money)
            if flag:
                print(msg)
                break
            else:
                print(msg)



#还款功能
@common.login_auth
def huankuan():
    while True:
        money=input('请输入还款金额：').strip()
        if not money.isdigit():
            print('必须是数字')
            continue
        else:
            money=int(money)
            msg=bank_interface.huankuan_interface(user_info['user'],money)
            print(msg)
            break


#转账功能
@common.login_auth
def zhuanzhang():
    while True:
        #1、输入目标用户
        to_user=input('请输入转账的用户：')
        #2、输入转账金额
        money=input('请输入转账的金额：')
        if not money.isdigit():
            print('金额需要是数字！')
            continue
        money=int(money)
        #3、调用转账接口
        flag,msg=bank_interface.zhuanzhang_interface(user_info['user'],to_user,money)
        if flag:
            print(msg)
            break
        else:
            print(msg)


#查看流水功能
@common.login_auth
def watch_liushui():
    money_water=bank_interface.liushui_interface(user_info['user'])
    if money_water:
        for i in money_water:
            print(i)


#购物功能
@common.login_auth

def go_shopping():
    #商品列表
    good_list=[
        #商品名，价格
        ['广东凤爪',50],
        ['笔记本',30],
        ['福气公仔',35],
        ['坦克',25]
    ]
    #定义空的购物车
    shopping_car={}
    #商品的总价
    cost=0
    #获取当前的用户金额
    user_bal=bank_interface.chakan_money_interface(user_info.get('user'))
    while True:
        #打印商品信息
        for index,goods in enumerate(good_list):
            print(index,goods)
        #用户输入商品编号进行商品选择
        choice=input('请输入商品编号：').strip()
        if choice=='q':
            break
        if not  choice.isdigit():
            print('必须是数字')
            continue
        choice=int(choice)
        good_name, good_price = good_list[choice]
        #加入购物车，统计商品数量
        if good_name in shopping_car:
            shopping_car[good_name] +=1
        else:
            shopping_car[good_name] =1
        #计算商品总价
        cost += good_price
        print(f'已将{good_name}加入购物车')
    # print(f'购物总花费{cost}元')
    #确认是否结算,y结算付钱，n不结算直接加入购物车

    while True:
        sure=input('是否确认购买，输入y/n').strip()


        if sure =='y':
            print(f'购物总花费{cost}元')
            # 结算：调用商品支付接口
            flag,msg=shop_interface.shop_pay_interface(
                user_info.get('user'),shopping_car,cost)
            if flag:

                print(msg)
            else:
                print(msg)
            break
        elif sure =='n':
        #不选择支付，就将商品添加到购物车中保存起来
            flag,msg=shop_interface.shopping_car_interface(
                user_info.get('user'),shopping_car
            )
            if flag:
                print(msg)
            else:
                print(msg)
            break
        else:
            print('输入错误，请看清楚')




#查看该人的购物车中的商品功能
@common.login_auth
def watch_shop_car():
    #查看该人的购物车中的商品
    shopping_car_goods=shop_interface.watch_shop_interface(user_info.get('user'))
    print(shopping_car_goods)


#注销功能
@common.login_auth
def zhuxiao():
    msg=user_interface.zhuxiao_interface(user_info['user'])

    print(msg)


func_dic={
    '1':register,
    '2':login,
    '3':check_money,
    '4':tixian,
    '5':huankuan,
    '6':zhuanzhang,
    '7':watch_liushui,
    '8':go_shopping,
    '9':watch_shop_car,
    '10':zhuxiao
}

def run():
    while True:
        func_mag="""
        1、注册
        2、登录
        3、查看额度
        4、提现
        5、还款
        6、转账
        7、查看流水
        8、购物功能
        9、查看购物车
        10、注销
        q、退出
        """
        print(func_mag)
        choice=input('请输入功能编号：q 退出').strip()
        if choice=='q':
            break
        if choice not in func_dic:
            print('输入不在功能范围内，请重新输入：')
            continue

        #执行下面选择的功能
        func_dic.get(choice)()













