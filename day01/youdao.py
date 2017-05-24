####有道词典不行了，网页换了


import urllib.request
import urllib.parse
import json

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null'
data = {}
head = {}
head[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'

data['i'] = 'i love you'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1495614981009'
data['sign'] = '4348af22b465ff3d45fc0103a317aef4'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'

data1 = urllib.parse.urlencode(data).encode('utf-8')

# i:i love you
# from:AUTO
# to:AUTO
# smartresult:dict
# client:fanyideskweb
# salt:1495614981009
# sign:4348af22b465ff3d45fc0103a317aef4
# doctype:json
# version:2.1
# keyfrom:fanyi.web
# action:FY_BY_CLICKBUTTON
# typoResult:true

req = urllib.request.Request(url,data1,head)
htr = urllib.request.urlopen(req)
html = htr.read().decode('utf-8')
# dict1 = json.load(html)##然后访问字典里面的翻译信息
print(html)
