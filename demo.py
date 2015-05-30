# -*- coding: UTF-8 -*- 
import urllib2
url = "http://www.qiushibaike.com/hot/page/1"
user_agent  = "Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)"
headers = { 'User-Agent' : user_agent }
#打开一个链接地址
#request = urllib2.Request(url,headers)
result = urllib2.urlopen(url,headers)
#引入html源代码
print result.read()

