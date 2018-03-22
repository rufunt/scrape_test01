import requests
from bs4 import BeautifulSoup


def get_html(url):
	r = requests.get(url)
	return r.text

def get_data(html):
		soup = BeautifulSoup(html, 'lxml')
		h1 = soup.find('div', id='content').find('div', id='dle-content').text
		return h1

def main():
	url = 'https://footballhd.ru/allnews/'
	print(get_data(get_html(url)))




if __name__ == '__main__':
	main()