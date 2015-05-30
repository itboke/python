
#coding=utf-8

import re
import urllib


x=0
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html
	
def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist 	
	
html = getHtml('http://tieba.baidu.com/p/2982551055')

list  = getImg(html)	
for imgurl in list:
	#print imgurl
	urllib.urlretrieve(imgurl,'%d.jpg' % x)
	x += 1