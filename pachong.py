#! /usr/bin/env python
#coding=utf-8
import urllib
import urllib2
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
url = "www.baidu.com"
print url
#调试函数
#try
#request = urllib2.Request(url)
response = urllib2.urlopen(url)
print response.read()

#except urllib2.URLError,e:
#print e.code
#print e.reason
        
        
        
    
