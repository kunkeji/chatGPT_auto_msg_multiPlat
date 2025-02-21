import json
import requests
API_URL = "https://api-inference.modelscope.cn/api-inference/v1/models/iic/nlp_rom_passage-ranking_chinese-base"
# 请用自己的SDK令牌替换{YOUR_MODELSCOPE_SDK_TOKEN}（包括大括号）
headers = {"Authorization": f"Bearer 69376002-a2ac-47a7-84a2-2c8ae9527bf6"}
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
payload = {"input": {"source_sentence": ["功和功率的区别"], "sentences_to_compare": ["功反映做功多少，功率反映做功快慢。", "什么是有功功率和无功功率?无功功率有什么用什么是有功功率和无功功率?无功功率有什么用电力系统中的电源是由发电机产生的三相正弦交流电,在交>流电路中,由电源供给负载的电功率有两种;一种是有功功率,一种是无功功率.", "优质解答在物理学中,用电功率表示消耗电能的快慢．电功率用P表示,它的单位是瓦特（Watt）,简称瓦（Wa）符号是W.电流在单位时间内做的功叫做电功率 以灯泡为例,电功率越大,灯泡越亮.灯泡的亮暗由电功率（实际功率）决定,不由通过的电流、电压、电能决定!"]}}
output = query(payload) 
print(output)