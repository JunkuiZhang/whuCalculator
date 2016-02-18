import requests
import bs4
import time
import urllib.parse as enco
import sqlite3
import re

class Cal:
	def __init__(self, user, password):
		self.user = user
		self.pwd = password
		self.initurl = "http://210.42.121.241"
		self.url = "http://210.42.121.241/servlet/Login"
		# self.gradeurl = "http://210.42.121.241/servlet/Svlt_QueryStuScore?year=0&term=&learnType=&scoreFlag=0&t="
		# curtime = time.strftime("%a %b %d %G ")
		# curtime = enco.quote(curtime)
		# self.gradeurl = self.gradeurl + curtime + time.strftime("%T") + "%20GMT+0800%20(%D6%D0%B9%FA%B1%EA%D7%BC%CA%B1%BC%E4)"
		self.stuurl = "http://210.42.121.241/stu/stu_index.jsp"
		self.gradeurl = "http://210.42.121.241/servlet/Svlt_QueryStuScore?year=0&term=&learnType=&scoreFlag=0&t=Thu%20Feb%2018%202016%2014:50:35%20GMT+0800%20(%D6%D0%B9%FA%B1%EA%D7%BC%CA%B1%BC%E4)"
		# self.gradeurl = "http://210.42.121.241/stu/stu_index.jsp"
		requestsheader = {
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Encoding": "gzip,deflate,sdch",
			"Accept-Language": "zh-CN,zh;q=0.8",
			"Cache-Control": "max-age=0",
			"Connection": "keep-alive",
			"Host": "210.42.121.241",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
		}
		initialre = requests.get(self.initurl, headers=requestsheader)
		self.initialcoo = initialre.cookies

	def getcaptche(self):
		__captche = "http://210.42.121.241/servlet/GenImg"
		__response0 = requests.get(__captche, cookies=self.initialcoo)
		self.cookies = __response0.cookies
		self.cotext = re.findall('kie (.*) for ', str(self.cookies))[0]
		__captcheimg = open("0.jpg", "wb")
		__captcheimg.write(__response0.content)
		__captcheimg.close()
		__captchecode = input("Enter the strings in the picture: ")
		return __captchecode
		# return cotext

	def work(self):
		postData = {
			"id": self.user,
			"pwd": self.pwd,
			"xdvfb": self.getcaptche()
		}
		requestHeader0 = {
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Encoding": "gzip,deflate,sdch",
			"Accept-Language": "zh-CN,zh;q=0.8",
			"Cache-Control": "max-age=0",
			"Connection": "keep-alive",
			"Cookie": self.cotext,
			"Content-Type": "application/x-www-form-urlencoded",
			"Host": "210.42.121.241",
			"Origin": "http://210.42.121.241",
			"Referer": "http://210.42.121.241/",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
		}
		# login_response = requests.post(self.url, data=postData, headers=requestHeader0, cookies=self.cookies)
		login_response = requests.post(self.url, data=postData, headers=requestHeader0)
		requestHeader1 = {
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Encoding": "gzip,deflate,sdch",
			"Accept-Language": "zh-CN,zh;q=0.8",
			"Cache-Control": "max-age=0",
			"Connection": "keep-alive",
			"Cookie": self.cotext,
			"Host": "210.42.121.241",
			"Referer": "http://210.42.121.241/",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
		}
		# response = requests.get(self.stuurl, cookies=login_response.cookies, headers=requestHeader1)
		response = requests.get(self.stuurl, headers=requestHeader1, cookies=login_response.cookies)
		print(response.text)
		# requestHeader1 = {
		# 	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		# 	"Accept-Encoding": "gzip,deflate,sdch",
		# 	"Accept-Language": "zh-CN,zh;q=0.8",
		# 	"Connection": "keep-alive",
		# 	"Cookie": "JSESSIONID=A3DD37B986483CA287140B1E3855E9EF.tomcat2",
		# 	"Host": "210.42.121.241",
		# 	"Referer": "http://210.42.121.241/stu/stu_score_parent.jsp",
		# 	# "Referer": "http://210.42.121.241/stu/stu_index.jsp",
		# 	"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
		# }
		# conn = requests.get(self.gradeurl, cookies=response.cookies, headers=requestHeader1)
		# conn = requests.get(self.gradeurl, headers=requestHeader1)
		# conn_text = conn.text
		# soup = bs4.BeautifulSoup(str(conn_text), "html.parser")
		# data = soup.find_all("tr")

		# connection = sqlite3.connect("MyGrade.db")
		# cur = connection.cursor()
		# cur.executescript('''
		# create table if not exists AllCourses(
		#
		# );
		# create table if not exists CourseTitle;
		# create table if not exists CourseClass;
		# create table if not exists CourseCredit;
		# create table if not exists CourseTName;
		# create table if not exists CourseYear;
		# create table if not exists CourseSemester;
		# create table if not exists CourseType;
		# create table if not exists CourseScore(
		# 	id integer autoincrement primary key not null;
		#	score integer not null
		# )
		# ''')

		# for item in data:
		# 	# soup_item = bs4.BeautifulSoup(str(item))
		# 	print("")
		# 	print("")
		# 	print(item)
		# print(response.headers)

while True:
	user = input("Enter your user name: ")
	password = input("Enter your password: ")

	if len(user) < 1:
		user = "2013301000021"
	if len(password) < 1:
		password = "zjk1995"

	c = Cal(user, password)
	c.work()