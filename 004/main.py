import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
	r = requests.get(url)
	if r.ok:
		return r.text
	print(r.status_code)


def refine_cy(s):
	# ТИЦ: 5555 -> ['ТИЦ', '5555']
	return s.split(' ')[-1]	


def write_csv(data):
		with open('football.csv', 'a') as f:
			writer = csv.writer(f)
			writer.writerow((data['title'], data['url'], data['snippet'], data['coment']))


def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')

	lists = soup.find_all('div', class_='sh_art')
	
	for div in lists:
		try:
			title = div.find('h2').find('u').text
		except:
			title = ''

		try:
			url = div.find('h2').find('a').get('href')
		except:
			url = ''

		try:
			snippet = div.find('p').text.strip()
		except:
			snippet = ''

		try:
			coment = div.find('b').text.strip()
		except:
			coment = ''	

		data = { 'title': title, 'url': url, 'snippet': snippet, 'coment': coment }


		write_csv(data)


def main():
	pattern = 'https://footballhd.ru/allnews/page/{}/'

	for i in range(1, 5):
		url = pattern.format(str(i))
		get_page_data(get_html(url))



if __name__ == '__main__':
	main()	