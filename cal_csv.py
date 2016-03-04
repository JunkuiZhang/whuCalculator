import requests
import bs4
import time
import urllib.parse as enco
import re
import csv
import os

# ==========================================================================
# At first, this program did not work.
# At last, I found its reason is just I misspelled the word "pwd" as "pws".
# Holy shit!!
# It wastes me almost 3 days to find the fucking solution!!
# ===========================================================================

class Cal:
	def __init__(self, user, password):
		self.user = user
		self.pwd = password
		self.url = "http://210.42.121.241/servlet/Login"
		self.gradeurl = "http://210.42.121.241/servlet/Svlt_QueryStuScore?year=0&term=&learnType=&scoreFlag=0&t="
		curtime = time.strftime("%a %b %d %G ")
		curtime = enco.quote(curtime)
		self.gradeurl = self.gradeurl + curtime + time.strftime("%T") + "%20GMT+0800%20(%D6%D0%B9%FA%B1%EA%D7%BC%CA%B1%BC%E4)"

	def getcaptche(self):
		__captche = "http://210.42.121.241/servlet/GenImg"
		headers = {
			"Host": "210.42.121.241",
			"Connection": "keep-alive",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",
			"Accept-Encoding": "gzip,deflate,sdch",
			"Accept-Language": "zh-CN,zh;q=0.8"
		}
		__response0 = requests.get(__captche, headers=headers)
		self.cookies = __response0.cookies
		self.cotext = re.findall('kie (.*) for ', str(self.cookies))[0]
		__captcheimg = open("0.jpg", "wb")
		__captcheimg.write(__response0.content)
		__captcheimg.close()
		__captchecode = input("Enter the strings in the picture: ")
		return __captchecode

	def work(self):
		postData = {
			"id": self.user,
			"pwd": self.pwd,
			"xdvfb": self.getcaptche()
		}
		requestHeader0 = {
			"Cookie": self.cotext,
			"Host": "210.42.121.241",
			"Origin": "http://210.42.121.241",
			"Referer": "http://210.42.121.241/",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
		}
		login_response = requests.post(self.url, data=postData, headers=requestHeader0, cookies=self.cookies)

		requestHeader1 = {
			"Cookie": self.cotext,
			"Host": "210.42.121.241",
			"Referer": "http://210.42.121.241/stu/stu_score_parent.jsp",
			# "Referer": "http://210.42.121.241/servlet/Login",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
		}
		conn = requests.get(self.gradeurl, cookies=login_response.cookies, headers=requestHeader1)

		conn_text = conn.text
		check = re.findall('captcha-img', str(conn_text))
		if check != []:raise ValueError("Invalid captcha input!!")
		soup = bs4.BeautifulSoup(str(conn_text), "html.parser")
		data = soup.find_all("tr")

		def getGPA(num):
			if float(num) >= 90: return 4.0
			elif float(num) >= 85: return 3.7
			elif float(num) >= 82: return 3.3
			elif float(num) >= 78: return 3.0
			elif float(num) >= 75: return 2.7
			elif float(num) >= 72: return 2.3
			elif float(num) >= 68: return 2.0
			elif float(num) >= 64: return 1.5
			else: return 1.0

		_credit = []
		_totalCredit = []
		_totalGPA = []
		if not os.path.exists("./Users"):
			os.makedirs("./Users")
		f = open("./Users/%s.csv" % self.user, "w", newline="")
		w = csv.writer(f)
		w.writerow(["Course", "Credit", "Class", "Name", "Type", "Year", "Semester", "Score"])
		for item in data:
			info = re.findall("<td>(.*)</td>", str(item))
			if info == []:
				continue
			title = info[1]
			_class = info[2]
			credit = info[3]
			name = info[4]
			type = info[6]
			year = int(info[7])
			semester = info[8]
			score = info[9]
			w.writerow([title, credit, _class, name, type, year, semester, score])
			if score == "":
				score = 1
				_totalCredit.append(credit)
			elif float(score) >= 60:
				_credit.append(credit)
				_totalGPA.append(getGPA(score) * float(credit))
			score = float(score)

			print(title, "  ", _class, "  ", credit, "  ", name, "  ", year, "  ", semester, "  ", score, "  ", type)
			print("==="*20)
		f.close()

		def sum0(list):
			summation = 0
			for num in list:
				summation += float(num)
			return summation

		print("Well done.")
		print("Your total credit for now is ", sum0(_credit))
		print("Your future credit is ", sum0(_credit) + sum0(_totalCredit))
		print("Your credit in this semester is ", sum0(_totalCredit))
		print("Your current GPA is ", sum0(_totalGPA)/sum0(_credit))




while True:
	user = input("Enter your user name: ")
	password = input("Enter your password: ")

	if len(user) < 1:
		user = "2013301000021"
	if len(password) < 1:
		password = "zjk1995"

	c = Cal(user, password)
	c.work()