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




def main():
	url = 'https://footballhd.ru/allnews/page/1/'
	print(get_html(url))



if __name__ == '__main__':
	main()	