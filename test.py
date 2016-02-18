import re
import requests

url0 = "http://210.42.121.241"
url1 = "http://210.42.121.241/servlet/Login"
url2 = "http://210.42.121.241/servlet/GenImg"
url3 = "http://210.42.121.241/stu/stu_index.jsp"

# headers = {
# 	"Host": "210.42.121.241",
# 	"Connection": "keep-alive",
# 	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
# 	"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",
# 	"Accept-Encoding": "gzip,deflate,sdch",
# 	"Accept-Language": "zh-CN,zh;q=0.8"
# }
# respon = requests.get(url0, headers=headers)
# cotext0 = re.findall('kie (.*) for ', str(respon.cookies))[0]
#
headers = {
	"Accept": "image/webp,*/*;q=0.8",
	"Accept-Encoding": "gzip,deflate,sdch",
	"Accept-Language": "zh-CN,zh;q=0.8",
	"Connection": "keep-alive",
	# "Cookie": cotext0,
	"Host": "210.42.121.241",
	"Referer": "http://210.42.121.241/",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
}
response0 = requests.get(url2, headers=headers)
captcheimg = open("0.jpg", "wb")
captcheimg.write(response0.content)
captcheimg.close()
captchecode = input("Enter the strings in the picture: ")

data = {
	"id": "2013301000021",
	"pws": "zjk1995",
	"xdvfb": captchecode
}
cotext = re.findall('kie (.*) for ', str(response0.cookies))[0]
requestsheader = {
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Encoding": "gzip,deflate,sdch",
			"Accept-Language": "zh-CN,zh;q=0.8",
			"Cache-Control": "max-age=0",
			"Connection": "keep-alive",
			# "Cookie": "JSESSIONID=ECD54F6E826CBFA8AFB1348C0CE5C20D.tomcat2",
			"Cookie": cotext,
			# "Content-Length": "40",
			"Content-Type": "application/x-www-form-urlencoded",
			"Host": "210.42.121.241",
			"Origin": "http://210.42.121.241",
			# "Referer": "http://210.42.121.241/",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
		}
response1 = requests.post(url1, data=data, headers=requestsheader, cookies=response0.cookies)

headers = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding": "gzip,deflate,sdch",
	"Accept-Language": "zh-CN,zh;q=0.8",
	"Cache-Control": "max-age=0",
	"Connection": "keep-alive",
	# "Cookie": "JSESSIONID=ECD54F6E826CBFA8AFB1348C0CE5C20D.tomcat2",
	"Cookie": cotext,
	"Host": "210.42.121.241",
	"Referer": "http://210.42.121.241/servlet/Login",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
}
response2 = requests.get(url3, headers=headers, cookies=response1.cookies)
print(response2.text)