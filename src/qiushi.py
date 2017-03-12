#coding=utf-8
import urllib,urllib2,re
from lxml import etree

#爬取链接
url = "http://www.qiushibaike.com/pic/"
headers = { 
	"User-Agent":	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
}
request = urllib2.Request(url,data=None,headers = headers)
opener = urllib2.urlopen(request)
#print opener
reader = opener.read()
#print reader#网页源代码
#数据处理
htmlEtree = etree.HTML(reader)
#print htmlEtree
xpaths = htmlEtree.xpath("//img")

#循环
for path in xpaths:
	imgPath = path.attrib['src']
	imgName = imgPath.rsplit("/",1)[1]
	print(imgPath,imgName)
	#name 文件名称 怎么样获取文件名称 
	#图片存放指定目录下  地址拼接
	try:
		urllib.urlretrieve(imgPath,"spider_img/%s"%imgName)
	except:
			pass
print('学不好python的另一个原因，因为有个逗比')