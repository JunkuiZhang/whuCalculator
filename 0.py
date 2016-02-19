x1 = 'cur.execute("insert or ignore into Course'
x2 = ') values (?)", ('
x3 = ' ,))'

y1 = 'cur.execute("select id from Course'
y2 = ' where '
y3 = ' = ?", ('
y4 = ', ))'

z1 = ' = cur.fetchone()[0]'

data = ["Title", "Credit", "Name", "Year", "Semester", "Score", "Type"]
for n in data:
	print(x1 + n + "(" + n.lower() + x2 + n.lower() + x3)
	print(y1 + n + y2 + n.lower() + y3 + n.lower() + y4)
	print(n.lower() + "_id" + z1)

import requests
import re

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

respon = requests.session()
res0 = respon.get(url2, headers=headers)

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

headers = {
			"Cookie": cotext,
			"Host": "210.42.121.241",
			"Origin": "http://210.42.121.241",
			"Referer": "http://210.42.121.241/",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
		}
res1 = respon.post(url1, data=data, headers=headers)

headers = {
	"Cookie": cotext,
	"Host": "210.42.121.241",
	"Referer": "http://210.42.121.241/servlet/Login",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
}
res2 = respon.get(url3, headers=headers)

print(res2.text)