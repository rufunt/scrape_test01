#app4.2
import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
	r = requests.get(url)
	if r.ok:
		return r.text
	print(r.status_code)


def write_csv(data):
	with open(nnm.csv, 'a') as f:
		writer = csv.writer(f)
		writer.writerow((data['title'], data['url'], data['snippet']))	

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')

	lists = soup.find_all('div', class_='mb10')

	for div in lists:
		try:
			title = div.find('h3').text.strip()
		except:
			title = ''

		try:
			url = div.find('h3').find('a').get('href')
		except:
			url = ''

		try:
			snippet = div.find('p').text.strip()
		except:
			snippet = ''	
        
		data = {'title': title,'url': url,'snippet': snippet }

		write_csv(data)


def main():
	url = 'http://itog.info/blogs/page1/'
	get_page_data(get_html(url))



if __name__ == '__main__':
	main()	
