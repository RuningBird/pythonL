####爬猫

import urllib.request

# httpResponse = urllib.request.urlopen('http://placekitten.com/g/500/600')
# cat_img = httpResponse.read()
# print(type(httpResponse))
# with open('e:/cat/cat_img.jpg','wb') as f:
#     f.write(cat_img)


#%%%%%%%%%%%%%%%%第二种写法
rqo = urllib.request.Request('http://placekitten.com/g/500/600')
httpR = urllib.request.urlopen(rqo)
cat_img1 = httpR.read()
# print(type(httpR))
# with open('e:/cat/cat_img1.jpg','wb') as f:
#     f.write(cat_img1)
print(httpR.geturl())
print(httpR.info())
print(httpR.getcode())