####爬猫

import urllib.request
httpResponse = urllib.request.urlopen('http://placekitten.com/g/500/600')
cat_img = httpResponse.read()
print(type(httpResponse))
with open('e:/cat/cat_img.jpg','wb') as f:
    f.write(cat_img)
