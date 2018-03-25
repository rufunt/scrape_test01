import requests
from bs4 import BeautifulSoup


def get_html(url):
	r = requests.get(url)
	return r.text

def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	h1 = soup.find('section').find('div', class_='item-pager').text
	print(h1)
	#return h1

def main():
	url = 'https://ask.fm/KatyaBrazhnik'
	print(get_data(get_html(url)))




if __name__ == '__main__':
	main()