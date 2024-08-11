
# AI_URL = "http://172.30.0.1:3000/api/v1/chat/completions"
# AI_KEY = "Bearer fastgpt-uD4XUlbxKegt0OTJmXo3ZP0Ro2OtfqPqV6HxaX2FMY70YttbwCAZ7ETB3x2Vd"


AI_CONTENT_TYPE = "application/json"
KEYWORD_FILE = "./data/keyword.json"
APP_NAME = "壳林智能客服"
SOUND_FILE ="./static/1.mp3"
APP_ICON_PATH="./static/image/icons/logo.png"
PDD_APP_CLASS_NAME="g_wszPDDWindowClass{E77EAED1-21E4-4F21-AE4C-50A6AE1E47A4}"               #拼多多平台类名
PDD_APP_TITLE="拼多多工作台"                    #拼多多平台标题
PDD_MSG_CLASS_NAME="MsgRemindDlg"               #拼多多消息提醒类名
PDD_MSG_TITLE="MsgStrengthenRemindDlg"                    #拼多多消息提醒标题
PDD_WINMSG_CLASS="Chrome Legacy Window"                 #拼多多信息框类名
PDD_WINNING_CLASS= "Chrome_RenderWidgetHostHWND"
PDD_WINNING_NAME= "提醒"

QN_APP_CLASS_NAME="Qt5152QWindowIcon"               #千牛平台类名
QN_APP_TITLE="千牛接待台"                    #千牛平台标题
QN_MSG_CLASS_NAME="Qt5152QWindowToolSaveBits"               #千牛消息提醒类名
QN_MSG_TITLE="消息提醒"                    #千牛消息提醒标题
QN_WINMSG_CLASS=" "                 #千牛信息框类名


DD_APP_CLASS_NAME=" "               #抖店平台类名
DD_APP_TITLE=" "                    #抖店平台标题
DD_MSG_CLASS_NAME="Chrome_WidgetWin_1"    #抖店消息提醒类名
DD_MSG_TITLE="抖店工作台-商家消息窗口"      #抖店消息提醒标题
DD_WINMSG_CLASS=" "                 #抖店信息框类名

PDD_SELECT, QN_SELECT, DD_SELECT = False, False, False
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 700
ICON_PATHS = ['./static/image/icons/home.png', './static/image/icons/chat.png', './static/image/icons/log.png', './static/image/icons/settings.png']
PLATFORMS = ["千牛", "拼多多", "抖店"]

# STRINGS_TO_REMOVE =[
#         "诈骗案件频发，谨防假客服欺诈！任何以不能下单或店铺有问题诱导卖家点击链接、文档或扫码跳转到微信、QQ、支付宝或其它非官方平台的行为都是欺诈。",
#         "谨防“订单卡单退款”类电信诈骗，请勿透露银行卡密码、验证码等信息！",
#         "阿里巴巴不会向用户索要任何密码信息，请注意保护您的隐私信息！",
#         "请勿使用阿里旺旺、千牛以外的其它聊天工具，以确保沟通、交易的安全。",
#         "消息可能包含存在未知风险的链接，请谨慎访问",
#         "您好像还没有配置消费者问到的常见问题回答，为了提升您的接待效率、减少顾客流失，建议您尽快完善此配置 立即配置",
#         "您接待过此消费者，为避免插嘴、抢答，机器人已暂停接待，>>点此【立即恢复接待】<<",
#         "机器人未找到对应的回复，点击添加",
#         "8-23点间，店铺需有客服在线，机器人才会接待消费者",
#         "没有更多了",
#         "使用“邀请下单”，可提前备注订单，轻松提升转化率！立即使用",
#         "您好像还没有配置消费者问到的常见问题回答，为了提升您的接待效率、减少顾客流失，建议您尽快完善此配置 立即配置",
#         "新消息"
#     ],