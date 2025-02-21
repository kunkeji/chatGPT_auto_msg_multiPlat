import sqlite3
from contextlib import closing
from PySide6.QtWidgets import QMessageBox,QWidget
import requests

# 服务器地址
SERVER_URL = 'https://kelin.kunkeji.com/api'

class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def execute(self, query, params=()):
        with closing(self._connect()) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(query, params)
                connection.commit()
                return cursor

    def fetchall(self, query, params=()):
        with closing(self._connect()) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()

    def fetchone(self, query, params=()):
        with closing(self._connect()) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()

    def insert(self, query, params):
        cursor = self.execute(query, params)
        return cursor.lastrowid

    def update(self, query, params):
        self.execute(query, params)

    def delete(self, query, params):
        self.execute(query, params)



class SystemInfo:
    def __init__(self, db):
        self.db = db

    def get_system_info(self):
        query = 'SELECT * FROM system_info'
        return self.db.fetchone(query)

    def update_system_info(self, **kwargs):
        # 构建更新字段和参数
        fields = ", ".join(f"{key} = ?" for key in kwargs)
        query = f"UPDATE system_info SET {fields} WHERE id = 1"  # 只有一条记录，假设 id = 1
        self.db.update(query, tuple(kwargs.values()))



class DatabaseManager:
    def __init__(self, db_name='app_data.db'):
        self.db_name = db_name
        self.db = Database(self.db_name)
    
    def show_login_expired_error(self):
        # 假设你没有直接访问到主窗口，你可以创建一个临时的 QWidget
        temp_widget = QWidget()
        QMessageBox.critical(temp_widget, "错误", "当前登录已过期，请重新登录")

    # 请求方法，包含鉴权
    def Ajax(self, url, headers=None, params=None, data=None, method='GET'):
        # 获取token
        token = self.get_system_info()[11]
        headers = {
            'Content-Type': 'application/json',
            'token': f'{token}'
        }
        url = f'{SERVER_URL}{url}'
        try:
            response = requests.request(method, url, headers=headers, params=params, data=data)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as err:
            # 判断登录是否过期
            if isinstance(err, requests.HTTPError) and err.response.status_code == 401:
                # 弹出提示框并提示用户重新登录

                self.show_login_expired_error()
                # 设置自动登录为0
                self.update_system_info(auto_login=0)

            raise Exception('请求失败:', err)

    def _operate_on_model(self, model_cls, method_name, *args, **kwargs):
        model = model_cls(self.db)
        method = getattr(model, method_name)
        return method(*args, **kwargs)

    def get_system_info(self):
        return self._operate_on_model(SystemInfo, 'get_system_info')

    def update_system_info(self, **kwargs):
        return self._operate_on_model(SystemInfo, 'update_system_info', **kwargs)


    def get_keywords(self):
        r = self.Ajax('/chatkeywords/list',params={'type':1})
        response_data = r.json()
        return response_data['data']

    def getkeyword(self, id):
        r = self.Ajax('/chatkeywords/getkeyword',params={'id':id})
        response_data = r.json()
        return response_data['data']

    def get_stoetkeywords(self, stortid):
        r = self.Ajax('/chatkeywords/storelist',params={'store_id':stortid})
        response_data = r.json()
        return response_data['data']

    def get_sensitive(self):
        r = self.Ajax('/chatkeywords/list',params={'type':2})
        response_data = r.json()
        return response_data['data']

    def add_keyword(self, keyword, content,store_id = 0,type = 1):
        r = self.Ajax('/chatkeywords/add',params={'key':keyword,'value':content,'store_id':store_id,'type':type})
        response_data = r.json()
        return response_data['data']

    def update_keyword(self, keyword_id, keyword, content):
        r = self.Ajax('/chatkeywords/update',params={'id':keyword_id,'key':keyword,'value':content},method='PUT')
        response_data = r.json()
        return response_data['data']

    def delete_keyword(self, keyword_id):
        r = self.Ajax('/chatkeywords/delete',params={'id':keyword_id},method='DELETE')
        response_data = r.json()
        return response_data['data']

    def get_userinfo(self,token):
        r =self.Ajax('/user/index')
        response_data = r.json()
        return response_data['data']

    def get_association(self, data):
        r = self.Ajax('/chats/detailsBc',params={
                'customer_id':data['fromid']['targetId'],

                'customer_nick':data['fromid']['nick'],
                'customer_service_id':data['toid']['targetId'],
                'customer_service_nick':data['toid']['nick'],
                'main_account_id':data['loginid']['havMainId'],
                'session_id':data['ccode']
            })
        response_data = r.json()
        return response_data['data']

    def add_association(self, data):
        r = self.Ajax('/chats/add',params={'customer_id':data['userid'],
                'customer_nick':data['username'],
                'customer_service_id':data['kefuid'],
                'customer_service_nick':data['kefuname'],
                'main_account_id':data['havMainId'],
                'product_id':data['product_id'],
                'session_id':data['ccode']
            })
        response_data = r.json()
        return response_data

    def get_goods(self, name):
        r = self.Ajax('/chatstore/getbyname',params={'name':name})
        response_data = r.json()
        return response_data['data']
        # return self._operate_on_model(Goods, 'get_goods', name)
    def save_chatlog(self, data):
        try:
            params = {
                'direction': data['direction'],
                'templateId': data['templateId'],
                'message_id': data['mcode']['messageId'],
                'info_id': data['mcode']['clientId'],
                'send_time': data['sendTime'],
                'session_id': data['ccode'],
                'fromid': data['fromid']['targetId'],
                'fromnick': data['fromid']['nick'],
                'fromname': data['fromid']['display'],
                'fromavatar': data['fromid']['portrait'],
                'toid': data['toid']['targetId'],
                'tonick': data['toid']['nick'],
                'toname': data['toid']['display'],
                'toavatar': data['toid']['portrait'],
                'summary': data['summary'],  
                'appkey': data['loginid']['appkey'],
                'loginname': data['loginid']['display'],
                'main_account_id': data['loginid']['havMainId'],
                'message_content': data['originalData']['message'],
                'message_type': data['originalData']['msgtype'],
                'info_type': data['originalData']['type'],
                'link_info': data['originalData']['urlinfo'],  
                'message_image_url': data['originalData']['pic'],

                'product_name': data['originalData']['goodsname'],  
                'product_url': data['originalData']['url'],
                'product_price': data['originalData']['price'], 
                'product_attributes': data['originalData']['itemSku'], 

                'video_url': data['originalData']['videourl'],
                'video_local_url': data['originalData']['locapath'], 
                'location_name':  data['originalData']['locationName'],  
                'longitude':  data['originalData']['longitude'], 
                'latitude':  data['originalData']['latitude'], 
                'status':  1 
            }
            r = self.Ajax('/chatdetails/add', params=params)
        except requests.exceptions.RequestException as e:
        # 适当的错误处理，例如记录日志、返回错误信息、抛出异常等
            print(e,'save_chatlog错误')

    def get_goodsByProductId(self, product_id):
        r = self.Ajax('/chatstore/getbyproductid',params={'id':product_id})
        response_data = r.json()
        return response_data['data']

    def get_goodsByid(self, id,type = 1):
        r = self.Ajax('/chatstore/getbyid',params={'id':id,'type':type})
        response_data = r.json()
        return response_data['data']
        # return self._operate_on_model(Goods, 'get_goodsByid', id)

    def add_goods(self, product_name ,product_url,store_name,details,welcome_word,product_id = None,type = 1,introduction= None,platform='tb'):
        r = self.Ajax('/chatstore/add',params={'product_name':product_name,'product_url':product_url,'store_name':store_name,'platform':platform,'details':details,'introduction':introduction,'welcome_word':welcome_word,'product_id':product_id,'type':type})
        response_data = r.json()
        return response_data

    def update_goods(self, id,product_name ,product_url,store_name,details,welcome_word,product_id = None,introduction= None,platform='tb'):
        r = self.Ajax('/chatstore/update',params={'id':id,'product_name':product_name,'product_url':product_url,'store_name':store_name,'platform':platform,'details':details,'introduction':introduction,'welcome_word':welcome_word,'product_id':product_id})
        response_data = r.json()
        return response_data

    def get_goodslist(self,type= 1):
        r = self.Ajax('/chatstore/getbyuserid',params={'type':type})
        response_data = r.json()
        return response_data['data']

    def delete_goods(self, id):
        r = self.Ajax('/chatstore/delete',params={'id':id},method='DELETE')
        response_data = r.json()
        return response_data['data']


