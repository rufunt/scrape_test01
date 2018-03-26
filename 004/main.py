import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
	r = requests.get(url)
	if r.ok:
		return r.text
	print(r.status_code)	




def main():
	url = 'https://yandex.ru/yaca/cat/Entertainment/'
	print(get_html(url))



if __name__ == '__main__':
	main()	