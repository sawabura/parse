import requests
from bs4 import BeautifulSoup
import selenium


def data_parsing():

	cookies = {
		'PHPSESSID': '03d5kc7iebpv3sc7anb369bb34',
	}

	headers = {
		'Accept': 'text/html, */*; q=0.01',
		'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
		'Connection': 'keep-alive',
		'Cookie': 'PHPSESSID=03d5kc7iebpv3sc7anb369bb34',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest',
	}

	params = {
		'lang': '1',
		'doc_dir': 'deu',
		'doc_num': '1',
	}

	for i in range(1, 150):
		try:
			params['doc_num'] = str(i)
			response = requests.get('http://uchisdarom.com.ua/player.php', params=params, cookies=cookies, headers=headers,
			                        verify=False)
			response.raise_for_status()
		except Exception as ex:
			print(ex)
		else:

			data = response.text
			with open("./file.html", "a+", encoding="utf-8") as file:
				file.write(data)


	print("the data is parsed successfully, gj")


def get_items_url(path_file):
	with open(path_file, "r",  encoding="utf-8") as file:
		src = file.read()

	soup = BeautifulSoup(src, "html.parser")
	items_p = soup.find_all("p")

	urls = []
	for item in items_p:
		try:
			item_url = item.find("a").get("href")

		except Exception as ex:
			print(ex)
			continue
		else:
			with open("./urls.txt", "a+", encoding="utf-8") as file:
				file.write(f"{item_url}\n")

def get_items_text(path_file):
	with open(path_file, "r",  encoding="utf-8") as file:
		src = file.read()

	soup = BeautifulSoup(src, "html.parser")
	items_p = soup.find_all("p")

	urls = []
	for item in items_p:
		try:
			item_url = item.find("a").get("download")

		except Exception as ex:
			print(ex)
			continue
		else:
			with open("./titles.txt", "a+", encoding="utf-8") as file:
				file.write(f"{item_url}\n")

def download_mp3(path, path2):
	with open(path, "r", encoding="utf-8") as file:
		url_list = [line.strip() for line in file]

	with open(path2, "r", encoding="utf-8") as file:
		titles_list = [line.strip().strip('.mp3') for line in file]
	print(titles_list)

	for url, title in zip(url_list, titles_list):
		response = requests.get(url=url)
		try:
			with open(f"{title}.mp3", "wb") as file:
				file.write(response.content)
		except Exception as ex:
			print(ex)
			continue



'''[Errno 2] No such file or directory: '/Users/Viktor Macgrey/Desktop/100DaysOfCode-master/parsing_data/Нем. Тема 22.5. Ботинки / туфли (Schuhe).mp3'

ПРОБЛЕМА В НАЗВАНИИ ЕСТЬ '/' по которому программа пытается найти что то'''


def main():

	# data_parsing()
	# get_items_url(path_file="./file.html")
	# get_items_text(path_file="./file.html")
	download_mp3(path="./urls.txt", path2="./titles.txt")


if __name__ == '__main__':
	main()


