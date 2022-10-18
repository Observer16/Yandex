import requests
from bs4 import BeautifulSoup

bank_id = 1771062 #ID банка на сайте banki.ru

url = 'https://www.banki.ru/services/questions-answers/?id=%d&p=1' % (bank_id) # url страницы
r = requests.get(url)
with open('/Users/vitalijaltunin/Documents/Python/YandexMap/test.html', 'w') as output_file:
  output_file.write(r.text)