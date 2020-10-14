from bs4 import BeautifulSoup, NavigableString
import requests
import pandas as pd

columns_name = ['name', 'season', 'status', 'tv_network', 'ano']
tvshows = pd.DataFrame(columns = columns_name)

for ano in range (2013, 2021):
  print(ano)
  headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36'}
  url = 'https://www.metacritic.com/feature/tv-renewal-scorecard-' + str(ano) + '-' + str(ano+1) + '-season'
  r = requests.get(url, headers = headers)
  soup = BeautifulSoup(r.text, 'html.parser')
  tables = soup.find_all('table')
  tv_network = soup.find_all('h2', class_ = 'special')


  for i in range(0, len(tables) - 1):
    rows = tables[i].find_all('tr')
    for row in rows:
      name = row.find('td', class_ = 'title')
      status = name.find_next('td')
      season = name.find('img', {"alt": "NEW"})
      if season is not None:
        # if there is an image in the title is because its the first season
        season = "1"
      else:
        season = name.find("span")
        if season is None:
          season = ""
        else:
          season = season.text
      if isinstance(name.contents[0], NavigableString):
        if str(name.contents[0]).strip() == '':
          name = name.contents[1].text
        else:
          name = name.contents[0]
      else:
        name = name.contents[0].text
      if status is None:
        status = ""
      else:
        status = status.text
      tvshow = {
        'name': str(name).strip(),
        'season': str(season).strip(),
        'status': str(status).strip(),
        'tv_network': str(tv_network[i].text).strip(),
        'ano': ano}
      tvshows = tvshows.append(tvshow, ignore_index = True)

  #ultima tabela
  rows = tables[-1].find_all('tr')
  for row in rows:
      name = row.find('td', class_ = 'title')
      season = name.find('img', {"alt": "NEW"})
      if season is not None:
        # if there is an image in the title is because its the first season
        season = "1"
      else:
        season = name.find("span")
        if season is None:
          season = ""
        else:
          season = season.text
      status = name.find_next('td')
      tv_network = row.find('td').find_next('td')
      if isinstance(name.contents[0], NavigableString):
        if str(name.contents[0]).strip() == '':
          name = name.contents[1].text
        else:
          name = name.contents[0]
      else:
        name = name.contents[0].text
      if status is None:
        status = ""
      else:
        status = status.text
      tvshow = {
        'name': str(name).strip(),
        'season': str(season).strip(),
        'status': str(status).strip(),
        'tv_network': str(tv_network.text).strip(),
        'ano': ano}
      tvshows = tvshows.append(tvshow, ignore_index = True)
file_name = './status/metacritic.csv'
tvshows.to_csv(file_name, index = False)





