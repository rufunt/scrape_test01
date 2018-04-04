import requests



def get_html(url):
	r = requests.get(url)
	if r.ok:
		return r.text
	print(r.status_code)







def main():
	url = 'https://coinmarketcap.com/all/views/all/'
	print(get_html(url))



if __name__ == '__main__':
	main()