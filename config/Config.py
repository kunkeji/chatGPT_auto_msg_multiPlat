class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Config(metaclass=SingletonMeta):
    # 定义所有配置项
    APP_RUN_STATE = False               #程序运行状态
    AI_CONTENT_TYPE = "application/json"
    KEYWORD_FILE = "./data/keyword.json"
    APP_NAME = "壳林智能客服"
    SOUND_FILE = "./static/1.mp3"
    APP_ICON_PATH = "./static/image/icons/logo.png"
    PDD_APP_CLASS_NAME = "g_wszPDDWindowClass{E77EAED1-21E4-4F21-AE4C-50A6AE1E47A4}"
    PDD_APP_TITLE = "拼多多工作台"
    PDD_MSG_CLASS_NAME = "MsgRemindDlg"
    PDD_MSG_TITLE = "MsgStrengthenRemindDlg"
    PDD_WINMSG_CLASS = "Chrome Legacy Window"
    PDD_WINNING_CLASS = "Chrome_RenderWidgetHostHWND"
    PDD_WINNING_NAME = "提醒"
    QN_APP_CLASS_NAME = "Qt5152QWindowIcon"
    QN_APP_TITLE = "千牛接待台"
    QN_MSG_CLASS_NAME = "Qt5152QWindowToolSaveBits"
    QN_MSG_TITLE = "消息提醒"
    QN_WINMSG_CLASS = " "
    DD_APP_CLASS_NAME = " "
    DD_APP_TITLE = " "
    DD_MSG_CLASS_NAME = "Chrome_WidgetWin_1"
    DD_MSG_TITLE = "抖店工作台-商家消息窗口"
    DD_WINMSG_CLASS = " "
    PDD_SELECT = False
    QN_SELECT = False
    DD_SELECT = False
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 700
    ICON_PATHS = ['./static/image/icons/home.png', './static/image/icons/chat.png', './static/image/icons/log.png', './static/image/icons/settings.png']
    PLATFORMS = ["千牛", "拼多多", "抖店"]
