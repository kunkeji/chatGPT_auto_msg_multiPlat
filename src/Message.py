from datetime import datetime
import os
import random
import requests
import pygame
from thefuzz import process, fuzz
from zhipuai import ZhipuAI
import json

class Message:
    
    def __init__(self,db,ui = None):
        self.db = db
        self.prompt = "你是一个资深的电商客服，你会根据产品的说明书准确的回答顾客所问的问题，并能根据顾客的反馈不断调整自己的服务态度和回复内容。但是在产品说明书中没有提到的或者没有产品说明书的情况下你不能按照自己的想法回答只能回答“请稍等”，本次的产品说明书内容是：" 

        # 获取config.json文件中的匹配度（pipeidu）的值
        with open('./config.json', 'r') as f:
            config = json.load(f)
        self.pipeidu = config['pipeidu']
        self.ui = ui
        print(self.pipeidu,'匹配度')

    #系统消息处理
    def sysmessage(self):
        return None
    
    # 添加随机表情
    def add_emoji(self,text):
        emojis = ["/:809","/:^x^","/:814","/:066","/:071","/:081","/:087","/:-F","/:lip","/:Y","/:803","/:008","/:073","/:813"]
        if len(emojis) > 0:
            emoji = random.choice(emojis)
            text += emoji
        return text

    # 关键词处理
    def extract_keys(self,keyword_list):
        if keyword_list is None:
            return {}
        return {keyword['key']: keyword['value'] for keyword in keyword_list}

    # 文本消息处理
    def textmessage(self,data):
        self.keywords = self.db.get_keywords()                         # 获取关键词列表
        self.keywords = self.extract_keys(self.keywords)
        # 首先判断是否存在商品名称
        msgcon = data["message"]
        if data["goodsinfo"]:
            goodinfo = data["goodsinfo"]
            if goodinfo:
                # 获取商品所属关键词列表
                stortKeywordList = self.db.get_stoetkeywords(goodinfo['id'])                         # 获取商品所属关键词列表
                stortKeywordList = self.extract_keys(stortKeywordList)
                # 进行店铺关键词匹配
                if stortKeywordList is not None:
                    matches = process.extractOne(msgcon, stortKeywordList.keys(), scorer=fuzz.token_set_ratio)
                    if matches and matches[1] > self.pipeidu:
                        # 获取匹配成功的关键词
                        matched_key = matches[0]
                        # 获取与该关键词关联的匹配信息
                        matching = stortKeywordList[matched_key]
                        self.local_save_chatlog(data['username'],msgcon,"关键词匹配："+matching,'关键词匹配')
                        return self.add_emoji(matching)
                    else:
                        matches = process.extractOne(msgcon, self.keywords.keys(), scorer=fuzz.token_set_ratio)
                        if matches and matches[1] > self.pipeidu:
                            # 获取匹配成功的关键词
                            matched_key = matches[0]
                            # 获取与该关键词关联的匹配信息
                            matching = self.keywords[matched_key]
                            self.local_save_chatlog(data['username'],msgcon,"关键词匹配："+matching,'关键词匹配')
                            return self.add_emoji(matching)
                        else:
                            msgdata = {
                                "ccode":data["ccode"],
                                "message":data["message"],
                                "knowledge":goodinfo['details']
                            }
                            sysinfo = self.db.get_system_info()
                            aireturn = self.aimassage(msgdata,sysinfo[9])
                            self.local_save_chatlog(data['username'],msgcon,aireturn,'说明书AI')
                            if "转人工" in aireturn or aireturn == "转人工":
                                self.play_sound()
                            else:
                                return aireturn
            else:
                if self.keywords is not None:
                    matches = process.extractOne(msgcon, self.keywords.keys(), scorer=fuzz.token_set_ratio)
                    if matches and matches[1] > self.pipeidu:
                        # 获取匹配成功的关键词
                        matched_key = matches[0]
                        # 获取与该关键词关联的匹配信息
                        matching = self.keywords[matched_key]
                        self.local_save_chatlog(data['username'],msgcon,"关键词匹配："+matching,'关键词匹配')
                        return self.add_emoji(matching)
                    else:
                        self.play_sound()
                        return None
                else:
                    self.play_sound()               # 播放提示音
                    return None                     # 返回None
        else:
            if self.keywords is not None:
                msgcon = data["message"]
                matches = process.extractOne(msgcon, self.keywords.keys(), scorer=fuzz.token_set_ratio)
                if matches and matches[1] > self.pipeidu:
                    # 获取匹配成功的关键词
                    matched_key = matches[0]
                    # 获取与该关键词关联的匹配信息
                    matching = self.keywords[matched_key]
                    self.local_save_chatlog(data['username'],msgcon,"关键词匹配："+matching,'关键词匹配')
                    return matching
                else:
                    msgdata = {
                        "ccode":data["ccode"],
                        "message":data["message"],
                        "knowledge":None
                    }
                    sysinfo = self.db.get_system_info()                                     # 获取系统信息
                    aireturn = self.aimassage(msgdata,sysinfo[10])
                    if "转人工" in aireturn or aireturn == "转人工":
                        self.play_sound()
                    else:
                        self.local_save_chatlog(data['username'],msgcon,aireturn,'通用AI')
                        return aireturn
            else:
                self.play_sound()               # 播放提示音
                return None                     # 返回None
            
    # 表情消息处理
    def facemessage(self,data):
        # 随机表情列表
        enumerate = ["/:-F","/:Y","/:809","/:087"]
        # 随机获取一个表情
        returnmsg = enumerate[int(len(enumerate)*random.random())]
        self.local_save_chatlog(data['username'],data,returnmsg,'表情消息')
        return returnmsg
    
    # 链接信息
    def urllinkmessage(self, data):
        url = data['message']
        id = url.split('id=')[-1]
        id = id.split('&')[0]
        goodinfo = self.db.get_goodsByProductId(id)
        if goodinfo is None:
            # 建立未完善商品名单
            id = data['url'].split('id=')[-1]
            id = id.split('&')[0]
            self.db.add_goods(data['goodsname'],data['url'],"","","",id,0)
            self.play_sound()
            return None
        elif goodinfo['welcome_word'] is None:
            self.play_sound()
            return None
        else:
            data['product_id'] = goodinfo['id']
            self.db.add_association(data)
            returnmsg = self.add_emoji(goodinfo['welcome_word']) 
            self.local_save_chatlog(data['username'],data['message'],returnmsg,'链接消息')
        return returnmsg                                                # 回复商品简介

    # 通过详情页发送的链接信息
    def linkmessage(self,data):
        goodsname = data['goodsname']
        url = data['url']
        id = url.split('id=')[-1]
        id = id.split('&')[0]
        goodinfo = self.db.get_goodsByProductId(id)
        if goodinfo is None:
            # 建立未完善商品名单
            self.db.add_goods(goodsname,data['url'],"","","",id,0)
            self.play_sound()
            return None
        elif goodinfo['welcome_word'] is None:
            self.play_sound()
            return None
        else:
            data['product_id'] = goodinfo['id']
            print(data,"新增对话关联记录")
            self.db.add_association(data)
            returnmsg = self.add_emoji(goodinfo['welcome_word']) 
            self.local_save_chatlog(data['username'],data['url'],returnmsg,'详情页进店')
        return returnmsg                                                 # 回复商品简介

    # 根据商品名称查询商品回复简介
    def getgoodsinfo(self,goodsname):
        return "商品简介"

    # 智谱AI平台消息处理
    def aimassage(self,data,prompt=None):
        # 定义智谱AI平台的API密钥
        api_key="40bd8ecca836bdfaeadf0568931d422c.B9k5ASggmy8gmCXf"
        # 从输入数据中提取会话id
        ccode = data["ccode"]                       # 会话id
        # 从输入数据中提取消息内容
        message = data["message"]                   # 消息内容
        # 从输入数据中提取知识内容
        knowledge = data["knowledge"]               # 知识内容
        # 构建prompt，结合实例的知识内容
        if knowledge is None:
            prompt = f"{prompt}"
        else:
            prompt = f"{prompt}{knowledge}"
       
        # 初始化智谱AI客户端
        client = ZhipuAI(api_key=api_key)
        # 发起消息完成请求，使用glm-4-flash模型
        response = client.chat.completions.create(
            model="glm-4-plus",
            messages=[
                {
                    # 系统角色，提供上下文和知识给AI
                    "role": "system",
                    "content": prompt
                },
                {
                    # 用户角色，模拟顾客的消息
                    "role": "user",
                    "content": f"顾客说：{message}"
                }
            ],
            # 设置生成参数，控制输出多样性
            top_p= 0.5,
            temperature= 0.8,
            # 设置最大生成token数
            max_tokens=1024,
            # 使用者的会话id，用于跟踪上下文
            user_id=ccode
        )
        # 返回AI生成的消息内容
        return response.choices[0].message.content
        if "转人工" in response.choices[0].message.content or response.choices[0].message.content == "转人工":
            self.play_sound()
        else:
            return response.choices[0].message.content
        
    # 链接爬取
    def fetch_page_content(self,url):
        try:
            # 发送GET请求
            response = requests.get(url)
            # 检查请求是否成功
            if response.status_code == 200:
                # 返回页面内容
                return response.text
            else:
                print(f"Failed to fetch the page. Status code: {response.status_code}")
                return None
        
        except requests.exceptions.RequestException as e:
            # 处理请求异常
            print(f"An error occurred while fetching the page: {e}")
            return None
    
    # 播放提示音
    def play_sound(self):
        # 初始化pygame的音频模块
        pygame.mixer.init()
        # 加载音频文件
        pygame.mixer.music.load('./static/1.mp3')
        # 播放音频文件
        pygame.mixer.music.play()
        # 等待音频播放完毕
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    # 本地聊天记录保存
    def local_save_chatlog(self,username,message,ai_reply,message_type):
        # 首先判断该用户的聊天记录是否存在，如果存在则续写，如果不存在则创建一个名为日期+客户昵称的聊天记录新文件。
        filename = f'./msglog/{datetime.now().date()}/{username}.txt'
        # 检查并创建目录
        directory = os.path.dirname(filename)
        self.ui.textEdit.append(f"{username}:{message}——>{ai_reply}")
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        # 现在可以安全地写入文件了
        try:
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(f'【{message_type}】[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]顾客{username}: {message} 【处理结果】： {ai_reply}\n\n')
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

    # 未识别消息记录
    def unrecognized_message(self,data):
        pass

    # 聊天记录保存
    def save_chatlog(self,data):
        # 保存到数据库
        self.db.save_chatlog(data)