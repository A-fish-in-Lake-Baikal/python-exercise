from aip import AipNlp
import json
import time

""" 你的 APPID AK SK """
APP_ID = '21663495'
API_KEY = 'SAoaTBzVOG76MnuFrmP3F1D7'
SECRET_KEY = 'xEq6KG8w73z4ZGp9jM5FprGXSNQDHwl0'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

text = "我叫马维畅"
text1 = "百度是一家高科技公司"

""" 调用词法分析 """
txt = client.lexer(text)
txt1 = client.lexerCustom(text1)
print(txt,txt1)
#print(json.jumps(txt,ensure_ascii=False, indent=4))
