
import win32con
import win32api
import time
import json
import pygame
import requests
import pyperclip
from fuzzywuzzy import process,fuzz

from config.Config import Config
from utils.utils import doClick

from config.Config import Config
from utils.utils import *

config = Config()
class MessageProcessor:
    def __init__(self, main_window):
        self.main_window = main_window
    def process_message(self, platform, hwnd_to_click, copy_offset):
        try:
            start_time = time.time()
            win32gui.ShowWindow(getattr(config, f"{platform.upper()}_APP_HWND"), win32con.SW_MAXIMIZE)
            clipboard_content = ''
            self.main_window.log_message(f"{platform}消息")
            doClick(hwnd_to_click, copy_offset[0], copy_offset[1])
            for _ in range(5):
                clipboard_content = copy_message(getattr(config, f"{platform.upper()}_APP_HWND"), "Chrome Legacy Window", 2)
                if clipboard_content:
                    break
            massage = getattr(self.main_window, f"{platform}_getquestionlist")(clipboard_content)
            end_time = self.replyToEachMessage(massage, platform)
            all_time = end_time-start_time
            self.main_window.log_message(f"本次耗时：{all_time}秒")




        except Exception as e:
            self.main_window.log_message(f"Error processing message for {platform}: {e}")
    
    # 信息处理
    def replyToEachMessage(self,massageList,pingtai):
        thisusernma = ''
        for item in massageList:
            if pingtai == 'pdd':
                thisusernma = self.main_window.ppd_username()
                message_text = item['usermsg']
            if pingtai == 'qn':
                thisusernma = item['name']
                message_text = item['massage']
            if message_text == '[图片信息]':
                pygame.init()
                pygame.mixer.music.load(config.SOUND_FILE)
                pygame.mixer.music.play()
                config.APP_RUN_STATE = False
                self.change_run_button_icon("run")
            else:
                with open(config.KEYWORD_FILE, 'r', encoding='utf-8') as f:
                    keywords = json.load(f)
                matches = process.extractOne(message_text, keywords.keys(), scorer=fuzz.token_set_ratio)
                if matches and matches[1] > 80:
                    matched_key = matches[0]
                    matching = keywords[matched_key]
                    if pingtai == 'pdd':
                        pdd_click_bottom_center_offset()
                    if pingtai == 'qn':
                        qn_click_bottom_center_offset()

                    pyperclip.copy(matching)
                    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
                    win32api.keybd_event(ord('V'), 0, 0, 0)
                    win32api.keybd_event(ord('V'), 0, win32con.KEYEVENTF_KEYUP, 0)
                    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(0.1)
                    win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
                    win32api.keybd_event(
                        win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
                    pyperclip.copy('')
                else:
                    with open('./config/config.json', 'r', encoding='utf-8') as f:
                        CONFIG = json.load(f)

                    if message_text:
                        url = CONFIG['AI_URL']
                        headers = {
                            'Authorization': 'Bearer '+CONFIG['AI_KEY'],
                            'Content-Type': config.AI_CONTENT_TYPE
                        }
                        data = {
                            "chatId": thisusernma,
                            "stream": False,
                            "detail": False,
                            "messages": [
                                {
                                    "content": message_text,
                                    "role": "user"
                                }
                            ]
                        }
                        response = requests.post(url, headers=headers, json=data)
                        response_json = response.json()
                        content = response_json['choices'][0]['message']['content']
                        
                        save_unmatched_dialog(message_text, content)

                        content = content.strip()
                        if content == '请稍等':
                            pygame.init()
                            pygame.mixer.music.load(config.SOUND_FILE)
                            pygame.mixer.music.play()
                            config.APP_RUN_STATE = False
                            self.main_window.change_run_button_icon("run")
                            break
                        if pingtai == 'pdd':
                            pdd_click_bottom_center_offset()
                        if pingtai == 'qn':
                            qn_click_bottom_center_offset()
                        time.sleep(0.1)
                        pyperclip.copy(content)
                        win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
                        win32api.keybd_event(ord('V'), 0, 0, 0)
                        win32api.keybd_event(ord('V'), 0, win32con.KEYEVENTF_KEYUP, 0)
                        win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
                        time.sleep(0.1)
                        win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
                        win32api.keybd_event(
                            win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
                        pyperclip.copy('')
        end_time = time.time()

        return end_time