####===代理方式爬虫
#############################################################
#1，参数是一个字典{类型：代理ip}
#####proxy_support = urllib.request.ProxyHandler({})
#2，定制，创建一个opener
#3，安装opener
####urllib.request.install_opener(opener)
#4,调用opener
#####opener.open(url)

import urllib.request
import random
url = 'http://ip138.com'
iplist = ['202.199.232.62:8998','125.33.252.244:9000']
# 1
proxy_dict = {'http':random.choice(iplist)}
proxy_support = urllib.request.ProxyHandler(proxy_dict)
# 2 也可以加head
opener = urllib.request.build_opener(proxy_support)
# 3
urllib.request.install_opener(opener)
# 4
rps = urllib.request.urlopen(url)

html = rps.read().decode('gb2312')
print(html)

