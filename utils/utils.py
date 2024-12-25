# src/utils.py
import os
import json
import win32gui
import win32con
import win32api
import time
import pyautogui
import pyperclip
from config.Config import Config

config = Config()

def doClick(hwnd, cx, cy):
    Long_position = win32api.MAKELONG(cx, cy)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, Long_position)
    time.sleep(0.1)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, Long_position)

def find_child_window(parent_handle, child_window_title, index=1):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumChildWindows(parent_handle, callback, hwnds)

    matched_hwnds = []
    for hwnd in hwnds:
        if win32gui.GetWindowText(hwnd) == child_window_title:
            matched_hwnds.append(hwnd)
        child_hwnd = find_child_window(hwnd, child_window_title, index)
        if child_hwnd:
            matched_hwnds.append(child_hwnd)

    if len(matched_hwnds) >= index:
        return matched_hwnds[index - 1]
    return None

def copy_message(fhwnd, zihwnd, index):
    hwnd = find_child_window(fhwnd, zihwnd, index)
    doClick(hwnd, 10, 10)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)
    doClick(hwnd, 10, 10)
    clipboard_content = pyperclip.paste()
    return clipboard_content

def pdd_click_bottom_center_offset():

    rect = win32gui.GetWindowRect(config.PDD_APP_HWND)
    x, y, w, h = rect
    x = w // 2
    y = h - 150
    doClick(config.PDD_APP_HWND,x,y)

def qn_click_bottom_center_offset():
    rect = win32gui.GetWindowRect(config.QN_APP_HWND)
    x, y, w, h = rect
    x = w // 2
    y = h - 75
    doClick(config.QN_APP_HWND,x,y)

def save_unmatched_dialog(question, answer):
    try:
        filepath = './data/new_keyword.json'
        if not os.path.exists(filepath):
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump({}, f, ensure_ascii=False, indent=4)
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                dialog_dict = json.load(f)
            except json.JSONDecodeError:
                dialog_dict = {}
        if not isinstance(dialog_dict, dict):
            dialog_dict = {}
        dialog_dict[question] = answer
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(dialog_dict, f, ensure_ascii=False, indent=4)
        # print(f"成功保存对话: {question} -> {answer}")
    except Exception as e:
        print(f"保存未匹配对话失败: {e}")