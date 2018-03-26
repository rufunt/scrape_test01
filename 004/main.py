import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
	r = requests.get(url)
	if r.ok:
		return r.text
	print(r.status_code)


def write_csv(data):
		with open('football.csv', 'a') as f:
			writer = csv.writer(f)
			pass


def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')

	lists = soup.find_all('div', class_='sh_art')
	
	for div in lists:
		try:
			name = div.find('h2').text
		except:
			name = ''
		print(name)	




def main():
	url = 'https://footballhd.ru/allnews/page/1/'
	get_page_data(get_html(url))



if __name__ == '__main__':
	main()	