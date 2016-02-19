import bs4
import re

data = open("0.txt", encoding="utf-8").read()
soup = bs4.BeautifulSoup(data, "html.parser")
items = soup.find_all("tr")
_credits = []
_totalCredit0 = []
_totalCredit1 = []
for item in items:
	print("="*20)
	info = re.findall("<td>(.*)</td>", str(item))
	if info == []:continue
	print(info)
	title = info[1]
	_class = info[2]
	credit = info[3]
	name = info[4]
	type = info[6]
	year = int(info[7])
	semester = info[8]
	score = info[9]
	_totalCredit0.append(credit)
	if score == "":continue
	_totalCredit1.append(credit)
	if float(score) >= 60: _credits.append(credit)
	print(title, "   ", credit, "   ", score)
	print("="*20)

def summation(x):
	summa = 0
	for num in x:
		summa += float(num)
	return summa

x = summation(_credits)
y1 = summation(_totalCredit0)
y2 = summation(_totalCredit1)
print("Your total credit is ", x)
print("Your future credit is ", x + y1 - y2)