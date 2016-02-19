import re
import requests
import json

url0 = "http://210.42.121.241"
url1 = "http://210.42.121.241/servlet/Login"
url2 = "http://210.42.121.241/servlet/GenImg"
url3 = "http://210.42.121.241/stu/stu_index.jsp"

headers = {
	"Host": "210.42.121.241",
	"Connection": "keep-alive",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",
	"Accept-Encoding": "gzip,deflate,sdch",
	"Accept-Language": "zh-CN,zh;q=0.8"
}
res0 = requests.get(url2, headers=headers)

headers = {
	# "Accept": "image/webp,*/*;q=0.8",
	# "Accept-Encoding": "gzip,deflate,sdch",
	# "Accept-Language": "zh-CN,zh;q=0.8",
	# "Connection": "keep-alive",
	# "Cookie": cotext0,
	# "Host": "210.42.121.241",
	# "Referer": "http://210.42.121.241/",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
}

img = open("0.jpg", "wb")
img.write(res0.content)
img.close()
captchecode = input("pic: ")

data = {
	"id": "2013301000021",
	"pwd": "zjk1995",
	"xdvfb": captchecode
}

cotext = re.findall('kie (.*) for ', str(res0.cookies))[0]

requestsheader = {
			# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			# "Accept-Encoding": "gzip,deflate,sdch",
			# "Accept-Language": "zh-CN,zh;q=0.8",
			# "Cache-Control": "max-age=0",
			# "Connection": "keep-alive",
			# "Cookie": "JSESSIONID=EB10CA2BC6B857689C62133166A54B75.tomcat2",
			"Cookie": cotext,
			# "Content-Length": "40",
			# "Content-Type": "application/x-www-form-urlencoded",
			"Host": "210.42.121.241",
			"Origin": "http://210.42.121.241",
			# "Referer": "http://210.42.121.241/",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
		}
res1 = requests.post(url1, data=data, headers=requestsheader, cookies=res0.cookies)

headers = {
	# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	# "Accept-Encoding": "gzip,deflate,sdch",
	# "Accept-Language": "zh-CN,zh;q=0.8",
	# "Cache-Control": "max-age=0",
	# "Connection": "keep-alive",
	# "Cookie": "JSESSIONID=EB10CA2BC6B857689C62133166A54B75.tomcat2",
	"Cookie": cotext,
	"Host": "210.42.121.241",
	"Referer": "http://210.42.121.241/servlet/Login",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
}
res2 = requests.get(url3, headers=headers, cookies=res1.cookies)

print(res2.text)
print(" ")