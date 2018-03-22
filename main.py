import requests
from bs4 import BeautifulSoup


def get_html(url):
	r = requests.get(url)
	return r.text

def main():
	url = 'https://wordpress.org/'
	print(get_html(url))




if __name__ == '__main__':
	main()