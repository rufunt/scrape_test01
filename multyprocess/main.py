import requests
from bs4 import BeautifulSoup



def get_html(url):
	r = requests.get(url)
	if r.ok:
		return r.text
	print(r.status_code)



def get_all_links(html):
	soup = BeautifulSoup(html, 'lxml')

	tds = soup.find('table', id='currencies-all').find_all('td', class_='currency-name')

	links = []

	for td in tds:
		a = td.find('a').get('href')
		links.append(a)

	return links		





def main():
	url = 'https://coinmarketcap.com/all/views/all/'
	print(get_html(url))



if __name__ == '__main__':
	main()