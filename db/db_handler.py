
import json
import os
from conf import settings
#查找用户数据
def select(username):
    user_path=os.path.join(settings.DB_PATH,f'{username}.json')
    if os.path.exists(user_path):
        with open(user_path,'r',encoding='utf8')as fa:
            user_dic=json.load(fa)
            return user_dic

#保存用户数据
def save(user_dic):
   user_path=os.path.join(settings.DB_PATH,f'{user_dic.get("username")}.json')
   with open(user_path,'w',encoding='utf8')as fa:
       json.dump(user_dic,fa)
       fa.flush()





