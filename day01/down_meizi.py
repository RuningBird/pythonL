#####################
# 从jandan网下载妹子图
import urllib.request
import os

def get_page(url):
    pass

def down_meizi(folder='ooxx', pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx'
    pagenumber = get_page(url);

    for i in range(pages):
        pagenumber -= 1
        page_url = url + 'page' + str(pagenumber) + 'comments'

