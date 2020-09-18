from bs4 import BeautifulSoup
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36'}
url = 'https://www.metacritic.com/feature/tv-renewal-scorecard-2019-2020-season'
r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
