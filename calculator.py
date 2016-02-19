import requests
import bs4
import time
import urllib.parse as enco
import sqlite3
import re

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
		self.gradeurl = "http://210.42.121.241/stu/stu_index.jsp"

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
			# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			# "Accept-Encoding": "gzip,deflate,sdch",
			# "Accept-Language": "zh-CN,zh;q=0.8",
			# "Cache-Control": "max-age=0",
			# "Connection": "keep-alive",
			"Cookie": self.cotext,
			# "Content-Type": "application/x-www-form-urlencoded",
			"Host": "210.42.121.241",
			"Origin": "http://210.42.121.241",
			"Referer": "http://210.42.121.241/",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
		}
		# login_response = requests.post(self.url, data=postData, headers=requestHeader0, cookies=self.cookies)
		login_response = requests.post(self.url, data=postData, headers=requestHeader0, cookies=self.cookies)

		requestHeader1 = {
			# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			# "Accept-Encoding": "gzip,deflate,sdch",
			# "Accept-Language": "zh-CN,zh;q=0.8",
			# "Connection": "keep-alive",
			"Cookie":self.cotext,
			"Host": "210.42.121.241",
			# "Referer": "http://210.42.121.241/stu/stu_score_parent.jsp",
			"Referer": "http://210.42.121.241/servlet/Login",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
		}
		conn = requests.get(self.gradeurl, cookies=login_response.cookies, headers=requestHeader1)
		# conn = requests.get(self.gradeurl, headers=requestHeader1)
		print(conn.text)

		# conn_text = conn.text
		# soup = bs4.BeautifulSoup(str(conn_text), "html.parser")
		# data = soup.find_all("tr")
		#
		# connection = sqlite3.connect("MyGrade.db")
		# cur = connection.cursor()
		# cur.executescript('''
		# create table if not exists AllCourses(
		# 	title integer not null,
		# 	class integer not null,
		# 	credit integer not null,
		# 	name integer not null,
		# 	year integer not null,
		# 	semester integer not null,
		# 	score integer not null,
		# 	type integer not null
		# );
		# create table if not exists CourseTitle(
		# 	id integer autoincrement primary key not null unique,
		# 	title text unique
		# );
		# create table if not exists CourseClass(
		# 	id integer autoincrement primary key not null unique,
		# 	class text unique
		# );
		# create table if not exists CourseCredit(
		# 	id integer autoincrement primary key not null unique,
		# 	credit text unique
		# );
		# create table if not exists CourseTName(
		# 	id integer autoincrement primary key not null unique,
		# 	name text unique
		# );
		# create table if not exists CourseYear(
		# 	id integer autoincrement primary ley not null unique,
		# 	year integer unique
		# );
		# create table if not exists CourseSemester(
		# 	id integer autoincrement primary key not null unique,
		# 	semester text unique
		# );
		# create table if not exists CourseType(
		# 	id integer autoincrement primary key not null unique,
		# 	type text unique
		# );
		# create table if not exists CourseScore(
		# 	id integer autoincrement primary key not null unique,
		# 	score integer not null
		# )
		# ''')
		#
		# for item in data:
		# 	soup_item = bs4.BeautifulSoup(str(item))
		# 	data = re.findall("<td>(.*)</td>", str(soup_item))
		# 	title = data[1]
		# 	_class = data[2]
		# 	credit = data[3]
		# 	name = data[4]
		# 	type = data[5]
		# 	year = int(data[6])
		# 	semester = data[7]
		# 	score = int(data[8])
		#
		# 	cur.execute("insert or ignore into CourseSemester(semester) values (?)", (semester ,))
		# 	cur.execute("select id from CourseSemester where semester = ?", (semester, ))
		# 	semester_id = cur.fetchone()[0]
		#
		# 	cur.execute("insert or ignore into CourseScore(score) values (?)", (score ,))
		# 	cur.execute("select id from CourseScore where score = ?", (score, ))
		# 	score_id = cur.fetchone()[0]
		#
		# 	cur.execute("insert or ignore into CourseType(type) values (?)", (type ,))
		# 	cur.execute("select id from CourseType where type = ?", (type, ))
		# 	type_id = cur.fetchone()[0]
		#
		# 	cur.execute("insert or ignore into CourseCredit(credit) values (?)", (credit ,))
		# 	cur.execute("select id from CourseCredit where credit = ?", (credit, ))
		# 	credit_id = cur.fetchone()[0]
		#
		# 	cur.execute("insert or ignore into CourseName(name) values (?)", (name ,))
		# 	cur.execute("select id from CourseName where name = ?", (name, ))
		# 	name_id = cur.fetchone()[0]
		#
		# 	cur.execute("insert or ignore into CourseYear(year) values (?)", (year ,))
		# 	cur.execute("select id from CourseYear where year = ?", (year, ))
		# 	year_id = cur.fetchone()[0]
		#
		# 	cur.execute("insert or ignore into CourseTitle(title) values (?)", (title ,))
		# 	cur.execute("select id from CourseTitle where title = ?", (title, ))
		# 	title_id = cur.fetchone()[0]
		#
		# 	cur.execute("insert or ignore into CourseClass(class) values (?)", (_class ,))
		# 	cur.execute("select id from CourseClass where class = ?", (_class, ))
		# 	class_id = cur.fetchone()[0]
		#
		# 	cur.execute("insert or replace into AllCourses(title, class, credit, name, year, semester, score, type) values (?, ?, ?, ?, ?, ?, ?, ?)", (title_id, class_id, name_id, year_id, semester_id, score_id, type_id))
		#
		# 	print(data)
		# connection.commit()

	def getInfo(self):
		conn = sqlite3.connect("MyGrade.db")
		cur = conn.cursor()
			# SELECT Track.title, Artist.name, Album.title, Genre.name
			# FROM Track JOIN Genre JOIN Album JOIN Artist
			# ON Track.genre_id = Genre.ID and Track.album_id = Album.id
			# AND Album.artist_id = Artist.id
			# ORDER BY Artist.name LIMIT 3



while True:
	user = input("Enter your user name: ")
	password = input("Enter your password: ")

	if len(user) < 1:
		user = "2013301000021"
	if len(password) < 1:
		password = "zjk1995"

	c = Cal(user, password)
	c.work()