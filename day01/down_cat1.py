####爬猫加time模块

import urllib.request
import time

# httpResponse = urllib.request.urlopen('http://placekitten.com/g/500/600')
# cat_img = httpResponse.read()
# print(type(httpResponse))
# with open('e:/cat/cat_img.jpg','wb') as f:
#     f.write(cat_img)


# #%%%%%%%%%%%%%%%%第二种写法
for i in range(10):
    rqo = urllib.request.Request('http://placekitten.com/g/500/600')
    httpR = urllib.request.urlopen(rqo)
    cat_img1 = httpR.read()
    print(type(httpR))
    dir = 'e:/cat/cat_img%s.jpg' % i
    with open(dir,'wb') as f:
        f.write(cat_img1)
time.sleep(1)