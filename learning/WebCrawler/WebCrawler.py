# !/user/bin/python3
# -*-coding:UTF-8-*-

from urllib import request

proxy_support = request.ProxyHandler({'http':'http://121.232.144.203:9000'})
opener = request.build_opener(proxy_support, request.HTTPHandler)
request.install_opener(opener)

response = request.urlopen("https://movie.douban.com/")
content = response.read().decode('UTF-8')
print(content)